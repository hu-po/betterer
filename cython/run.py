"""
This directory shows how to wrap a C++ Class using Cython so it is callable
in Python. This follows the tutorial on Evan's Blog.

Build the C++ and Cython classes by running the setup file:
>  python setup.py build_ext --inplace

Sources:
- [1] https://ecurtin2.github.io/2016/08/21/Wrap-C++-Class-Using-Cython/
"""



# Import the Cython Class
import ClassWrapper
instance = ClassWrapper.WrapperClass(5)
print(instance.Mydouble)

# Use our getters and setters to access cpp_double
instance.Mydouble= 34.5
print(instance.Mydouble)

# The void func changes the value of the cpp_double from within the cpp class
instance.void_func()
print(instance.Mydouble)

# We can also just call functions from the instance
print(instance.func(3.5, 10))
