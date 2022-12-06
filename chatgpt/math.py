import numpy as np


# CoPilot
# function that calculates the GeLU activation function
def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

# ChatGPT
# write a python function that calculates the GeLU activation function
# can you use numpy instead of math

def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))

# CoPilot
# a function that creates a 3 layer MLP that is 10 neurons wide
def create_mlp():
    return np.random.rand(10, 10, 10)

# ChatGPT
# write a python function that creates a 3 layer MLP that is 10 neurons wide
def create_3layer_mlp(input_shape):
  model = tf.keras.Sequential()
  
  # First hidden layer
  model.add(tf.keras.layers.Dense(10, input_shape=input_shape, activation='relu'))
  
  # Second hidden layer
  model.add(tf.keras.layers.Dense(10, activation='relu'))
  
  # Output layer
  model.add(tf.keras.layers.Dense(10, activation='softmax'))
  
  return model

# Winner is ChatGPT