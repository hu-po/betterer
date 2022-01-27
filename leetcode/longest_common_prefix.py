class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # bad inputs
        if not strs:
            return ''
        
        for word in strs:
            if not word:
                return ''
        
        # toy case
        if len(strs) == 1:
            return strs[0]
        
        """
        Test cases:
        ['abc', 'ab'] -> 'ab'
            prefix = 'a', 
            
        ['abc', 'ab', ''] -> ''
        
        """
        
        # time O(N*M) ~ O(N*M)
        # space O(1 + 1 + M) ~ O(M)
        # M is length of maximum word
        # N is length of strs (number of words)
        
        char_i: int = 0
        word_i: int = 0
        prefix: str = strs[word_i][char_i]
        while char_i < len(strs[word_i]):
            if not strs[word_i]:
                return ''
            if not prefix[-1] == strs[word_i][char_i]:
                break
            word_i += 1
            if word_i == len(strs):
                word_i = 0
                char_i += 1
                if char_i == len(strs[word_i]):
                    prefix += ' '    
                else:
                    prefix += strs[word_i][char_i]
        return prefix[:-1]
