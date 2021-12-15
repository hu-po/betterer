class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # Space O(N + 1 + 1 +) ~ O(N)
        # Time O(1 + 1 + N*(1) + N) ~ O(N)
        
        # Edge cases
        # empty string, string of length 1
        if not s:
            return -1
        if len(s) == 1:
            return 0
        
        # Algo
        lowest_index: Dict[str : int] = {}
            
        for i, char in enumerate(s):
            if lowest_index.get(char, None) is None:
                lowest_index[char] = i
            else:
                # Already there
                lowest_index[char] = -1
        
        single_char_found: bool = False
        min_index: int = len(s)
            
        for char, index in lowest_index.items():
            if index == -1:
                continue
            elif index < min_index:
                single_char_found = True
                min_index = index
        
        # Return
        # index of first non-repeating character
        # -1 if it does not exist
        return min_index if single_char_found else -1