from typing import Set, List

class Solution:
    def decodeString(self, s: str) -> str:
        
        # Space O(N + N + C + C) ~ O(N)
        # Time O(N*(C + C + C)) ~ O(N)
        
        # edge cases
        # empty string
        if not s:
            return None
        
        # algo
        # in-place?
        # Stack
        
        out: str = ''
        stack: List = []
            
        mult: str = ''
        enco: str = ''

        for char in s:
            if char == "]":
                _out = stack.pop()
                _mult = stack.pop()
                out = _out + int(_mult) * out
            elif char =="[":
                stack.append(mult)
                stack.append(out)
                out = ''
                mult = ''
            elif char.isdigit():
                mult += char 
            else:
                out += char
        
        # input string always valid
        # no digits, only digits are for k
        
        # k[encoded_str] repeated k times
        # k guaranteed positive int
        
        # return decoded string
        return out
