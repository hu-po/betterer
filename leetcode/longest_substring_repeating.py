from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # longest substring without repeating characters
        
        # what are some inputs, what are bad ones
        
        """
        possible inputs:
            None
            1
            ''
            'a'
            'aw'
            'lOoooO'
            'aaallll'
        """
        
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        # Time O(1 + 1 + 1 + N*(1 + 1 + 1)) ~ O(N)
        # Space O(1 + 1 + N) ~ O(N)
        
        longest_substring: int = 0
        substring_start: int = 0
        chars: Dict = {}
        for i in range(len(s)):
            if chars.get(s[i], None) is not None and substring_start <= chars[s[i]]:    
                substring_start = chars[s[i]] + 1
            else:
                longest_substring = max(longest_substring, i - substring_start + 1)
            chars[s[i]] = i
            

        return longest_substring
        
