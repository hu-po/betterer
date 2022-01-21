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


def main(
    test: bool = True
):
    if test:
        print(f'TINY TESTING MODE')
    # batch size training data minibatch 
    batch_size = 2 if test else 128
    # dimmensionality k of the query and key vectors
    dim_k = 2 if test else 64
    # dimmensionality v of the value vector
    dim_v = 2 if test else 64
    # dimmensionality h (number of heads in multi-head attention)
    dim_h = 2 if test else 8
    
    # these would be coming from a previous layer, and would be normalized
    # through layer norm or batch norm, hence the nice values
    mu, sigma = 0, 1

    # Query (q) and Key (k) vectors have dimmensionality k
    q = np.random.normal(loc=mu, scale=sigma, size=(batch_size, dim_h, dim_k))
    k = np.random.normal(loc=mu, scale=sigma, size=(batch_size, dim_h, dim_k))
    
    # Values (v) has dimmentionality v
    v = np.random.normal(loc=mu, scale=sigma, size=(batch_size, dim_h, dim_v))

    jax_multi_head_attention(q, k, v, dim_k)
    torch_multi_head_attention(q, k, v, dim_k)


def print_evaluation(_func : Callable) -> Callable:
    """ Provide memory and runtime prints for a transformer function. """
    def wrapped(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        out = _func(*args, **kwargs)
        print('\n\n\n')
        print(f'{_func.__name__}')
        print('\n\n\n')
        print(f'{_func.__name__} runtime was {time.time() - start_time} seconds.')
        print(f'{_func.__name__} used {tracemalloc.get_traced_memory()}')
        print(f'{_func.__name__} output is: {out}')
        print('\n\n\n')
        tracemalloc.stop()
    return wrapped


@print_evaluation
def jax_multi_head_attention(
    q: np.ndarray,
    k: np.ndarray,
    v: np.ndarray,
    dim_k: int,
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
    out = out / math.sqrt(dim_k)
    # softmax

    # multiply by values


    # out: jnp.DeviceArray = jax.nn.gelu(seq)
    # convert back to numpy array
    return np.array(out)


@print_evaluation
def torch_multi_head_attention(
    q: np.ndarray,
    k: np.ndarray,
    v: np.ndarray,
    dim_k: int,
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
    out = out / math.sqrt(dim_k)
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

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--test",
        help="Use lower dimmensions and batch sizes for quick testing.",
        action="store_true")
    args = parser.parse_args()

    main(test=args.test)
