# S-combinator from Combinatory Logic
# Sxyz = xz(yz)

from typing import Callable, List

def s_comb(x : Callable, y : Callable,  z : List[int]) -> List[int]:
  return x(y(_z), _z) for _z in z
  
def add(x, y): return x + y
def add_one(x): return x + 1
  
 assert s_comb(add, add_one, [1, 2, 3]) == [3, 5, 7]
