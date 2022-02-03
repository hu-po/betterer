from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return true if t is anagram of s
        # anagram -> word with original characters re-arranged
        
        # check inputs, edge cases
        if not s or not t:
            return False
        
        if not len(s) == len(t):
            return False
        
        # time O(N + N) ~ O(N) where N is the length of s
        # space O(N) ~ O(N) where N is length of s
        
        s: Dict[str, int] = collections.Counter([char for char in s])
        
        for char in t:
            if not char in s:
                return False
            else:
                s[char] -= 1
                if s[char] < 0:
                    return False
        
        return True
        
