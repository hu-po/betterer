from typing import Dict, Set

class Solution:    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Space O(N + C + N) ~ O(N)
        # Time O(C + C + N + N*(C + N)) ~ O(N*N)
        
        # Edge Cases
        # String can be empty, or length 1
        # length s2 < length s1
        if not s1 or not s2:
            return False
        
        if len(s2) < len(s1):
            return False
        
        # Algo
        # permutation - set
        # creating a set using s1 and checking each sub-string in s2
 
        # Second set where you keep track of "characters so far"
    
        # Recursion where once you hit a character in s1, you send then next len(s1) characters to the same substring method
        
        s1_dict: Dict[str : int] = {}
        for c in s1:
            if s1_dict.get(c, None) is not None:
                s1_dict[c] += 1
            else:
                s1_dict[c] = 1
        
        def is_permutation(s3: str) -> bool:
            # print(f'in is_permutation, got {s3}')
            s1_dict_copy = copy.deepcopy(s1_dict)
            # print(f'in is_permutation, {s1_dict_copy}')
            for c in s3:
                s1_dict_copy[c] -= 1
                if s1_dict_copy[c] < 0:
                    return False
            return True
                    
        counter: int = 0        
        for i, char in enumerate(s2):           
            if s1_dict.get(char, None) is not None:     
                counter += 1
                if counter >= len(s1) and is_permutation(s2[(i-len(s1))+1:i+1]):
                    return True
            else:
                counter = 0
        
        # Return
        # boolean - does s2 contain permutation sub-string of s1
        return False