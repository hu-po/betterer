from typing import Set
from queue import LifoQueue

class Solution:
    def calculate(self, s: str) -> int:
        
        # dictionary with possible valid characters
        # integer division shouldn't have remainders
        
        # PEMDAS - stack
        # parenthesis, exponents, mult, div, add, sub
        
        # edge cases: empty string, invalid string
        # open parenthesis that never close
        # characters that don't exist in simple math, etc
        # Double digit integers?
        if not s:
            return None
            
        # Algo
        # Space O(C + N + C) ~ O(N)
        # Time O(C + C + N*(C) + N) ~ O(N)
        
        ops: Set = set(['*', '/', '+', '-'])
        stack: LifoQueue = LifoQueue()
        s += '+'
        num: int = 0
        op: str = None
        for char in s:
            if char.isdigit():
                num = 10*num + int(char)
            elif char == ' ':
                pass
            elif char in ops:
                if not op or op == '+':    
                    stack.put(num)
                elif op == '*':
                    stack.put(stack.get() * num)
                elif op == '/':
                    stack.put(int(stack.get() / num))
                elif op == '-':
                    stack.put(-num)
                num = 0
                op = char
            else:
                raise ValueError(f'Invalid char {char} in string for calculator {s}')
                
        solution: int = 0
        while not stack.empty():
            solution += stack.get()
        return solution
      
