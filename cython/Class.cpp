#include "Class.h"

double my_namespace::MyCppClass::cpp_func(double x, int i) {
    double val = 0.0;
    for(int j = 0; j < i; j++) {
        val += x;
    }
    return val;
}

void my_namespace::MyCppClass::cpp_void_func() {
    cpp_double = 1.2;
}
