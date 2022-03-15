from hypothesis import given
from hypothesis.strategies import integers

def add(a, b):
    return a + b

@given(integers(), integers())
def test_add(a, b):
    print(f' testing with a {a} and b {b}')
    assert add(a, b) == a + b
    assert add(a, b) == add(b, a)

if __name__ == '__main__':
    test_add()