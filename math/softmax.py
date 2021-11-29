# Softmax three different ways
#
#   softmax(Xi) = exp(Xi) / sum(exp(Xij))
#

# Softmax with Numpy
import numpy as np

def softmax_np(x : np.ndarray) -> np.ndarray:
    x -= np.max(x) # Numerical stability trick
    return np.exp(x) / np.sum(np.exp(x))

x = np.array([1, 10, -10])
print(f'NUMPY in {x} out {softmax_np(x)}')

# Softmax with Tensorflow
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

def softmax_tf(x : tf.Tensor) -> tf.Tensor:
    x -= tf.math.reduce_max(x)
    return tf.exp(x) / tf.math.reduce_sum(tf.exp(x))

x = tf.constant([1, 10, -10], dtype=tf.float32)
print(f'TENSORFLOW in {x} out {softmax_tf(x)}')

# import torch as T
import torch as T

def softmax_torch(x : T.TensorType) -> T.TensorType:
    x -= T.max(x)
    return T.exp(x) / T.sum(T.exp(x))

x = T.tensor([1, 10, -10])
print(f'PYTORCH in {x} out {softmax_torch(x)}')