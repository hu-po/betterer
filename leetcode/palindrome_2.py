class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # check inputs, edge cases
        
        if not s or len(s) < 1:
            return True
        
        # time.O(1 + 1 + 1 + 0.5*N) ~ O(N) where N is length of string s
        # space.O(1 + 1) ~ O(1)
        
        si: int = 0
        ei: int = len(s) - 1
        while si < ei:
            # skipping non alphabet characters
            while not (s[si].isalpha() or s[si].isnumeric()):
                si += 1
                if si == ei:
                    break
            if si == ei:
                break
            while not (s[ei].isalpha() or s[ei].isnumeric()):
                ei -= 1
                if si == ei:
                    break
            if si == ei:
                break
            # check to make sure characters are the same
            if not s[si].lower() == s[ei].lower():
                return False
            ei -= 1
            si += 1
        return True
        
        
