class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # return start indices of p's anagrams in s, can return in any order
        
        # anagram is contains all the letters but in possibly different order
        
        # bad inputs
        """
        '', None
        
        'abab', 'baa' -> [0]
        
        
        """
        
        if not s or not p:
            return []
        
        if len(p) > len(s):
            return []
        
        # do upper and lowercase count?
        
        
#         char_counts_p: Dict[str, int] = {}
#         for char in p:
#             if char_counts_p.get(char, None) is not None:
#                 char_counts_p[char] += 1
#             else:
#                 char_counts_p[char] = 1
        
        
#         # lets move a sliding window of length p along s
#         for i in range(len(p), len(s) + 1):
#             char_counts_s: Dict[str, int] = {}
#             for j in range(i- len(p), i+1):
#                 if char_counts_s.get(char, None) is not None:
#                     char_counts_s[char] += 1
#                 else:
#                     char_counts_s[char] = 1
#             if char_counts_s == char_counts_p:
#                 anagram_starts.append(i)
                
        # make a Dict of number of letters in p and beginning of s
        counts_p: Dict[str, int] = collections.Counter(p)
        counts_s: Dict[str, int] = collections.Counter(s[:len(p)])
            
        # initialize the final returned list of starting indices
        anagram_starts: List[int] = []
            
        for i in range(len(s) - len(p) + 1):
            
            # print(f'counts_s {counts_s}')
            # print(f'counts_p {counts_p}')

            # check to see if the count dictionaries are the same
            if counts_s == counts_p:
                anagram_starts.append(i)
            
            # un-count the first character
            counts_s[s[i]] -= 1
            if counts_s[s[i]] <= 0:
                del counts_s[s[i]]
            
            # don't let sliding window go past limit
            if i + len(p) > len(s) - 1:
                break
            
            # count the new last character
            if counts_s.get(s[i + len(p)], None) is None:
                counts_s[s[i + len(p)]] = 1
            else:
                counts_s[s[i + len(p)]] += 1
            
        return anagram_starts
        
