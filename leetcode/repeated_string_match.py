class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        # repeat string a so that b is substring of a
        # if not possible, return -1
        
        """
        a="",b="a" -> -1
        
        a="",b="" -> 0
        
        a="a",b="" -> 0
        
        a="a",b="a" -> 1
        
        a="a",b="ab" -> -1
        
        a="a",b="aa" -> 
        
        a="a",b="aba"
        
        a="ab",b="baba"
        
        """
        
        # time O(1 + N? + 1 + 3) ~ O(1) where N is length of longest string a & b
        # space O(1 + 1 + ) ~ O(1)
        
        # check inputs, edge cases
        
        # b is empty string
        if not b:
            return 0
        
        # b is not empty, but a is empty
        if not a:
            return -1
        
        # b is just a single character
        if b in a:
            return 1
        
        # don't share letters
        if not set(b).issubset(set(a)):
            return -1
        
        # replace all instances of a in b?
        # repeat a a couple times, if b in a return true, else return false
        repeats: int = 1
        _a: str = a
        while repeats <= 3 or len(_a) <= 2*len(b):
            _a += a
            repeats += 1
            if b in _a:
                return repeats

        return -1
        
        
