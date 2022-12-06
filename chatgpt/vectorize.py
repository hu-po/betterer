import cProfile
import numpy as np
import uuid
import random

# CoPilot
# PROMPT: "a function to sum the elements of a numpy array"

def my_function(a, b):
    return (a - b) ** 2

# map the function my_function to the elements of two numpy arrays
def vectorize(a, b):
    return np.vectorize(my_function)(a, b)

# A function to find the squared distance between elements in two numpy arrays
def squared_distance(a, b):
    return np.sum((a - b) ** 2)

# ChatGPT
# PROMPT: ""

# define the function that we want to map to the arrays' elements
def my_function(a, b):
    return (a - b) ** 2

# use numpy.vectorize to create a new function that can be applied to numpy arrays
vec_my_function = np.vectorize(my_function)


if __name__ == "__main__":

    # For vectorization there is no winner
    # the result is a tie!