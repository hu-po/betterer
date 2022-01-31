class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0
        
        if not haystack or not needle or len(needle) > len(haystack):
            return -1
    
        for h in range(len(haystack) - len(needle) + 1):
            if haystack[h:h+len(needle)] == needle:
                return h
        return -1
