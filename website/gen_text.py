from transformers import BloomTokenizerFast, BloomForCausalLM
import torch


def generate_text(
    model_name: str,
    prompt: str,
    num_tokens_generated: int,
    search_type: str,
    temperature: float = 0.8,
) -> str:
    """ Generate text using the model and tokenizer. """

    tokenizer = BloomTokenizerFast.from_pretrained(model_name)
    model = BloomForCausalLM.from_pretrained(model_name)

    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    if search_type == "greedy":
        # chooses the next word at each timestep t+1 that has the highest predicted probability of following the word at t.
        outputs = model.generate(
            inputs["input_ids"],
            max_new_tokens=num_tokens_generated,
            temperature=temperature,
        )
    elif search_type == "beam":
        # keeps track of the n-th (num_beams) most likely word sequences and outputs the most likely sequence.
        outputs = model.generate(
            inputs["input_ids"],
            max_new_tokens=num_tokens_generated,
            # temperature=temperature,
            # do_sample=True,
            num_beams=2,
            no_repeat_ngram_size=2,
            early_stopping=True,
        )
    elif search_type == "topktopp":
        outputs = model.generate(
            inputs["input_ids"],
            max_new_tokens=num_tokens_generated,
            temperature=temperature,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )
    else:
        # the next word is chosen randomly based on its conditional probability distribution (von Platen, 2020). In Top-k, we choose the k most likely words, and then redistribute the probability mass amongst them before the next draw. Top-p adds an additional constraint to top-k, in that we’re choosing from the smallest set of words whose cumulative probability exceed p.
        raise ValueError("Invalid search type")

    return tokenizer.decode(outputs[0])


if __name__ == "__main__":

    context: str = "I co-founded a company in the machine learning space using synthetic data to improve computer vision. I hired and managed the technical team as the Chief Technology Officer. I have designed, trained and analyzed deep reinforcement learning agents deployed on real world robotic systems. I have worked at Google Brain, Amazon Robotics, and Silicon Valley startups. I graduated from CMU with a master's degree in Robotics and dual degrees in Physics and Mechanical Engineering. I have experience with PyTorch, Tensorflow, MuJoCo, Unity, Unreal Engine, Python, C#, C++. I am experimenting with protein folding and large language models."

    # With BPE tokenization, the number of words is roughly 3x the number of tokens
    num_words_to_generate: int = 50
    num_tokens_to_generate: int = 3 * num_words_to_generate

    for model_name in [
        # "bigscience/bloom-560m",
        # "bigscience/bloom-1b1",
        # "bigscience/bloom-1b7",
        "bigscience/bloom-3b",
    ]:
        for search_type in [
            # "greedy",
            "beam",
            "topktopp",
        ]:
            for preprompt in [
                "I am available for consulting work ",
                "Je suis disponible pour du conseil technique ",
                "Soy disponible para trabajo de consultoría ",
                # "Mis intereses son ",
                # "В мои интересы входит ",     
            ]:
                for temperature in [
                    # 0.3,
                    0.8,
                    # 1.0
                ]:
                    prompt: str = f"{context} {preprompt}"
                    text: str = generate_text(
                        model_name, prompt, num_tokens_to_generate, search_type, temperature=temperature)
                    # import pdb; pdb.set_trace()
                    text = text.lstrip(context)
                    print(f"Model: {model_name}")
                    print(f"Search type: {search_type}")
                    print(f"Temperature {temperature}")
                    print(text)
                    print('\n\n')
