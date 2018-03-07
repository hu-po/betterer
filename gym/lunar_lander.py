import time
from collections import deque
import torch
import gym
import numpy as np


# Sources
# [1] https://github.com/openai/gym/blob/master/gym/envs/box2d/lunar_lander.py
# [2] https://github.com/ShangtongZhang/DeepRL

class ActorNet(torch.nn.Module):

    def __init__(self, state_dim=8, hidden_size=16, action_dim=2,
                 action_gate=torch.nn.Softmax(),
                 action_scale=1.0,
                 non_linear=torch.nn.ReLU(),
                 batch_norm=False,
                 use_gpu=True):
        super(ActorNet, self).__init__()
        self.non_linear = non_linear
        self.batch_norm = batch_norm
        self.use_gpu = use_gpu
        self.action_gate = action_gate
        self.action_scale = action_scale

        # Build the actual network
        self.layer1 = torch.nn.Linear(state_dim, hidden_size)
        self.layer2 = torch.nn.Linear(hidden_size, hidden_size)
        self.layer3 = torch.nn.Linear(hidden_size, action_dim)
        if self.batch_norm:
            self.bn1 = torch.nn.BatchNorm1d(hidden_size)
            self.bn2 = torch.nn.BatchNorm1d(hidden_size)
        self.init_weights()

    def init_weights(self):
        # Initialize with bounded uniform distribution for last layer (constant 0 bias)
        bound = 3e-3
        torch.nn.init.uniform(self.layer3.weight.data, -bound, bound)
        torch.nn.init.constant(self.layer3.bias.data, 0)
        # Initialize the other layers with xavier (still constant 0 bias)
        torch.nn.init.xavier_uniform(self.layer1.weight.data)
        torch.nn.init.constant(self.layer1.bias.data, 0)
        torch.nn.init.xavier_uniform(self.layer2.weight.data)
        torch.nn.init.constant(self.layer2.bias.data, 0)

    def forward(self, x):
        x = torch.autograd.Variable(torch.Tensor(x))
        x = self.non_linear(self.layer1(x))
        if self.batch_norm:
            x = self.bn1(x)
        x = self.non_linear(self.layer2(x))
        if self.batch_norm:
            x = self.bn2(x)
        x = self.layer3(x)
        # Use optional gate and scaling for action
        if self.action_gate:
            x = self.action_gate(x)
        x = self.action_scale * x
        return x


class Policy(object):

    def __init__(self, lr=0.01, gamma=0.95):
        self.gamma = gamma  # Reward decay
        # Use an actor net as the model
        self.model = ActorNet()
        self.optimizer = torch.optim.RMSprop(self.model.parameters(), lr)
        # Episode specific data (cleared after each backprop)
        self.obs, self.actions, self.outputs, self.rewards = deque(), deque(), deque(), deque()
        self.action = None  # Single action (per step)

    def store(self, obs, action, reward):
        # Push the values into episode queues
        self.obs.append(obs)
        self.actions.append(action)
        self.rewards.append(reward)

    def step(self, obs):
        output = self.model.forward(obs)
        self.outputs.append(output)
        return output.cpu().data.numpy()

    def learn(self):
        # # Convert the queues into lists
        # actions, rewards, outputs = list(self.actions), list(self.rewards), list(self.outputs)
        # # Get the discounted reward from the epoch
        # cumulative = 0
        # loss = 0
        # for i in reversed(range(len(rewards))):
        #     cumulative = cumulative * self.gamma + rewards[i]
        #     cumulative_tensor = torch.autograd.Variable(torch.FloatTensor([cumulative]), requires_grad=False)
        #     actions_tensor = torch.autograd.Variable(torch.from_numpy(actions[i]), requires_grad=False)
        #     loss += - cumulative_tensor * (outputs[i] - actions_tensor)
        # loss.backward()
        # Convert the queues into lists
        actions = np.array(list(self.actions))
        rewards = list(self.rewards)
        outputs = list(self.outputs)
        # Get the discounted reward from the epoch
        discounted_rewards = np.zeros_like(rewards)
        cumulative = 0
        loss = torch.autograd.Variable()
        for i in reversed(range(len(rewards))):
            cumulative = cumulative * self.gamma + rewards[i]
            discounted_rewards[i] = cumulative
        # Normalize discounted reward
        discounted_rewards += np.mean(discounted_rewards)
        discounted_rewards /= np.std(discounted_rewards)
        actions_var = torch.autograd.Variable(torch.from_numpy(actions), requires_grad=False)
        loss = torch.nn.CrossEntropyLoss(weight=discounted_rewards)
        output = loss(outputs[i], actions_var)
        output.backward()
        # Take a gradient step using the optimizer
        self.optimizer.zero_grad()
        self.optimizer.step()
        # Clear the episode specific data
        self.obs, self.actions, self.outputs, self.rewards = deque(), deque(), deque(), deque()


def epoch(env, policy, min_rate=None, render=True):
    obs = env.reset()
    done = False
    # Counter variables for number of steps and total episode time
    epoch_tic = time.clock()
    num_steps = 0
    while not done:
        step_tic = time.clock()
        if render:
            env.render()
        # Use the previous observation to get an action from policy
        action = policy.step(obs)
        # Step the environment and push outputs to policy
        obs, reward, done, _ = env.step(action)
        policy.store(obs, action, reward)
        step_toc = time.clock()
        step_time = step_toc - step_tic
        if min_rate and step_time < min_rate:  # Sleep to ensure minimum rate
            time.sleep(min_rate - step_time)
        num_steps += 1
    # Total elapsed time in epoch
    epoch_toc = time.clock()
    epoch_time = epoch_toc - epoch_tic
    print('Episode complete (%s steps in %.2fsec), final reward %s ' % (num_steps,
                                                                        epoch_time,
                                                                        reward))
    policy.learn()


def experiment(env, policy, num_epochs=100):
    for _ in range(num_epochs):
        epoch(env, policy, min_rate=0.01)


if __name__ == '__main__':
    # Create lunar lander environment
    env = gym.make('LunarLanderContinuous-v2')

    # Action is two floats [main engine, left-right engines].
    # Main engine: -1..0 off, 0..+1 throttle from 50% to 100% power. Engine can't work with less than 50% power.
    # Left-right:  -1.0..-0.5 fire left engine, +0.5..+1.0 fire right engine, -0.5..0.5 off
    print('Action Space')
    print('     dim: ', env.action_space)
    print('     range %s to %s' % (env.action_space.high, env.action_space.low))

    # Observation space, according to source:
    # state = [
    #     (pos.x - VIEWPORT_W / SCALE / 2) / (VIEWPORT_W / SCALE / 2),
    #     (pos.y - (self.helipad_y + LEG_DOWN / SCALE)) / (VIEWPORT_W / SCALE / 2),
    #     vel.x * (VIEWPORT_W / SCALE / 2) / FPS,
    #     vel.y * (VIEWPORT_H / SCALE / 2) / FPS,
    #     self.lander.angle,
    #     20.0 * self.lander.angularVelocity / FPS,
    #     1.0 if self.legs[0].ground_contact else 0.0,
    #     1.0 if self.legs[1].ground_contact else 0.0
    # ]
    print('Observation space')
    print('     action space: ', env.observation_space)
    print('     range %s to %s' % (env.observation_space.high,
                                   env.observation_space.low))

    policy = Policy()
    experiment(env, policy)
