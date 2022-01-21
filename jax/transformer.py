"""
Transformer from scratch in JAX and PyTorch.

http://peterbloem.nl/blog/transformers
https://www.youtube.com/watch?v=tIvKXrEDMhk
https://arxiv.org/pdf/2112.05682.pdf
https://github.com/pytorch/pytorch/blob/master/torch/nn/modules/transformer.py

"""

from typing import Callable
import numpy as np
import tracemalloc
import time
import math
import jax
from jax import numpy as jnp
import torch


def main():
    # input sequence (batch, seq, feature)
    batch_size = 1
    dk = 2 # dimmensionality k
    feat_size = 4
    mu, sigma = 0, 1

    # Query (q) and Key (k) vectors have dimmensionality k
    q = np.random.normal(loc=mu, scale=sigma, size=(batch_size, dk, feat_size))
    k = np.random.normal(loc=mu, scale=sigma, size=(batch_size, dk, feat_size))
    
    # Values vector has dimmentionality 
    v = None

    jax_self_attention(q, k, v, dk)
    torch_self_attention(q, k, v, dk)


def print_evaluation(_func : Callable) -> Callable:
    """ Provide memory and runtime prints for a transformer function. """
    def wrapped(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        _func(*args, **kwargs)
        print(f'{_func.__name__} transformer runtime was {time.time() - start_time} seconds.')
        print(f'{_func.__name__} transformer used {tracemalloc.get_traced_memory()}')
        tracemalloc.stop()
    return wrapped


@print_evaluation
def jax_self_attention(
    q: np.ndarray,
    k: np.ndarray,
    v: np.ndarray,
    dk: int,
    **kwargs,
) -> np.ndarray:
    """
        Self-Attention block implemented in JAX.
    """
    # convert input numpy sequence to tensor
    q: jnp.DeviceArray = jnp.array(q)
    k: jnp.DeviceArray = jnp.array(k)
    out: jnp.DeviceArray = jnp.dot(q, jnp.transpose(k, axes=(0, 2, 1)))
    # normalize by square root of dimmensionality
    out = out / math.sqrt(dk)
    # softmax

    # multiply by values


    # out: jnp.DeviceArray = jax.nn.gelu(seq)
    # convert back to numpy array
    return np.array(out)


@print_evaluation
def torch_self_attention(
    q: np.ndarray,
    k: np.ndarray,
    v: np.ndarray,
    dk: int,
    **kwargs,
) -> np.ndarray:
    """
        Self-Attention block implemented in PyTorch.
    """
    # convert input numpy sequence to tensor
    q: torch.Tensor = torch.from_numpy(q)
    k: torch.Tensor = torch.from_numpy(k)
    out: torch.Tensor = torch.dot(q, torch.transpose(k, 2, 1))
    # normalize by square root of dimmensionality
    out = out / math.sqrt(dk)
    # softmax

    # multiply by values


    # activation = torch.nn.GELU()
    # out: torch.Tensor = activation(seq)
    # transformer_model = torch.nn.Transformer(
    #     nhead=num_heads, num_encoder_layers=num_encoder_layers)
    # out = transformer_model(seq, tgt)
    # convert back to numpy array
    return out.detach().cpu().numpy()


if __name__ == '__main__':
    main()
