class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        """
            s: str
            return True if s can be a palindrome after deleting at most one character
            
            two-pointer
            one in front and one in back, check for sameness and exit if more than one difference
            
            test case:
            s='abc'
            i=0
            j=2
            deleted=False
                0<2
                    a==c
                        mid = 1
                        return s[1:2] == s[2:2] or s[0:1] == s[1:1]
                        return 'b' == '' or 'a' == ''
                        return False or False
                        return False
                    
                    
        """
        
        # check inputs and edge cases
        if not s:
            return False
        
        if len(s) == 1:
            return True
        
        # time O(N / 2) ~ O(N) where N is length of string s
        # space O(1 + 1 + 1) ~ O(1)
        
        # two-pointers
        i: int = 0
        j: int = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                mid: int = int(len(s) / 2)
                return s[i+1:mid] == s[mid:j] or s[i:mid] == s[mid:j-1]
        return True
                    
