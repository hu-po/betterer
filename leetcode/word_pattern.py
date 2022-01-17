from typing import Dict, Set

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # Time O(1 + 1 + N *(1 + 1 + 1 + 1 + 1)) ~ O(N)
        # Space O(N + N + N) ~ O(N)
        
        # check for bad inputs
        if not s or not pattern:
            return False
        
        # split string into words (only letters? uppercase? special characters?)
        words: List[str] = s.split(' ')
        
        # not enough words to match pattern
        if not len(words) == len(pattern):
            return False
        
        # hash table of pattern lookup
        pattern_lookup: Dict[str, str] = {}
        
        # what codes have already been used?
        codes: Set = set()
            
        for word, code in zip(words, pattern):
            if pattern_lookup.get(word, None) is None:
                if code in codes:
                    return False
                pattern_lookup[word] = code
                codes.add(code)
            elif not pattern_lookup[word] == code:
                return False
            
        return True
