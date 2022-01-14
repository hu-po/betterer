"""
Transformer from scratch in JAX and PyTorch.

http://peterbloem.nl/blog/transformers
https://www.youtube.com/watch?v=tIvKXrEDMhk
https://arxiv.org/pdf/2112.05682.pdf
https://github.com/pytorch/pytorch/blob/master/torch/nn/modules/transformer.py

"""

import numpy as np
import tracemalloc
import time
import jax
from jax import numpy as jnp
import torch


def main():
    # input sequence (batch, seq, feature)
    batch_size = 10
    seq_size = 32
    feat_size = 4
    mu, sigma = 0, 0.1

    # query vectors
    dim_query = 12

    # Use the same input sequence for both functions
    seq = np.random.normal(loc=mu, scale=sigma, size=(
        batch_size, seq_size, feat_size))

    jax_transformer(name='JAX')
    torch_transformer(name='PyTorch')


def print_evaluation(func):
    """ Provide memory and runtime prints for a transformer function. """
    def wrapped(*args, **kwargs):
        name = kwargs.get('name', 'DEFAULT')
        tracemalloc.start()
        start_time = time.time()
        wrapped(*args, **kwargs)
        print(f'{name} transformer runtime was {time.time() - start_time} seconds.')
        print(f'{name} transformer used {tracemalloc.get_traced_memory()}')
        tracemalloc.stop()
    return wrapped


@print_evaluation
def jax_transformer(
    seq: np.ndarray,
    num_heads: int = 2,
    num_encoder_layers: int = 2,
) -> np.ndarray:
    """
        Transformer block implemented in JAX.
    """
    out = seq
    return out


@print_evaluation
def torch_transformer(
    seq: np.ndarray,
    num_heads: int = 2,
    num_encoder_layers: int = 2,
) -> np.ndarray:
    """
        Transformer block implemented in PyTorch.
    """
    seq = torch.from_numpy(seq)
    transformer_model = torch.nn.Transformer(
        nhead=num_heads, num_encoder_layers=num_encoder_layers)
    out = transformer_model(seq, tgt)
    return out.detach().cpu().numpy()


if __name__ == '__main__':
    main()
