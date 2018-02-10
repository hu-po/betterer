# Define the cpp class that will be wrapped
cdef extern from "Class.h" namespace "my_namespace":

    cdef cppclass MyCppClass:
        MyCppClass() except +

        #Attributes
        double cpp_double
        double cpp_public

        #Methods
        double cpp_func(double x, int i)
        void cpp_void_func()

# The actual wrapped class you can call from within Python
cdef class WrapperClass:
    cdef MyCppClass* C_Class

    # Constructor
    def __cinit__(self):
        self.C_Class = new MyCppClass()

    # Destructor
    def __dealloc__(self):
        del self.C_Class

    # Python Constructor
    def __init__(self, value):
        self.Mydouble = value

    # Python function wrapper for Cpp function
    def func(self, x, i):
        # Convert input to correct ctype
        cdef double c_x = x
        cdef int c_i = i
        # Call the cpp function
        val = self.C_Class.cpp_func(c_x, c_i)
        return val

    # Python function wrapper for Cpp function
    def void_func(self):
        self.C_Class.cpp_void_func()

    def python_func(self, x, y):
        return x == y

    # Getter and setter functions to access C class properties
    def get_cpp_double(self):
        return self.C_Class.cpp_double

    def set_cpp_double(self, value):
        cdef double c_val = value
        self.C_Class.cpp_double = c_val

    Mydouble = property(get_cpp_double, set_cpp_double)