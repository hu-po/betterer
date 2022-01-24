class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # all capital letters 
        # all lowercase letters
        # only first letter is capital
        
        # return true if capitals usage is correct
   

        # Time O(1 + 1 + N) ~ O(N)
        # Space O((N + N)) ~ O(N)
        
        # check bad inputs
        if not word:
            return False
        
        if len(word) == 1:
            return True
        
        if word[0].isupper():
            return all(char.isupper() for char in word[1:]) or \
                   all(char.islower() for char in word[1:])
        else:
            return all(char.islower() for char in word[1:])
