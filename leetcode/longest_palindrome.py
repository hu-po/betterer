    def longestPalindrome(self, s: str) -> str:
        
        # is the input properly formatted?
        if not s or len(s) <= 1:
            return s
        
        # # find the brute force solution O(N**2)
        # # palindrome is same forwards and backwards
        # longest_palindrome: int = 0
        # for i, char in enumerate(s):
        #     for j, charj in enumerate(s[j:]):
        #         middle = (j - i) // 2
        #         if s[i:middle] == reversed(s[middle:j]):
        #             longest_palindrome = max(longest_palindrome, j - i)
        # return longest_palindrome
    
        # Is there a recursive solution? DP mindfuck
        # rather than moving starting point of palindrome, move the "pivot"
        # check for equality of characters on either side of the pivot
        longest_pal_len: int = 1
        longest_pal: str = s[0]
        for i in range(len(s)):
            char_pivot_pal_len: int = 1
            cent_pivot_pal_len: int = 0
            for j in range(1, max(i+1, len(s)-i)):
                # Char is pivot
                if i-j >= 0 and i+j < len(s) and not char_pivot_pal_len == -1:
                    if s[i-j] == s[i+j]:
                        char_pivot_pal_len += 2
                        if char_pivot_pal_len >= longest_pal_len:
                            longest_pal_len = char_pivot_pal_len
                            longest_pal = s[i-j:i+j+1]
                    else:
                        char_pivot_pal_len = -1
                # Center pivot
                if i-j+1 >= 0 and i+j < len(s) and not cent_pivot_pal_len == -1:
                    if s[i-j+1] == s[i+j]:
                        cent_pivot_pal_len += 2
                        if cent_pivot_pal_len >= longest_pal_len:
                            longest_pal_len = cent_pivot_pal_len
                            longest_pal = s[i-j+1:i+j+1]
                    else:
                        cent_pivot_pal_len = -1
                # Check for break condition
                if cent_pivot_pal_len == -1 and char_pivot_pal_len == -1:
                    break
        return longest_pal
                    
                
#         # behavior at the end
#         cbab
#         i = 3, j = min(i + 1, len(s) - i)
                
#         # character is pivot
#         cbabp
#         i = 2, j = 1, check 1 and 3 are the same? check 0 and 4 are the same?
#         j = 1 -> check i - j and i + j -> len + 2
#         j = 2 -> check i - j and i + j -> len + 2
        
#         # pivot inbetween characters
#         cbaabp
#         i = 2, j = 1
#         check 2 and 3 are the same?
#         check 1 and 4 are the same?
#         check that 0 and 5 are the same?
#         j = 1 -> check i - j + 1 and i + j -> len + 2
#         j = 2 -> check i - j + 1 and i + j -> len + 2
#         j = 3 -> check i - j + 1 and i + j 
        
