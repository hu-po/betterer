from typing import Dict

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        # nums: List[int]
        # k: int 
        
        # return unique k-diff pairs
        # pairs is abs(x1-x2) = k
        # pairs are indices
        
        # check inputs, edge cases
        if not nums:
            return 0
        
        if k < 0:
            return 0
        
        """
        test cases
        [3,1,4,1,5], k=2
        lookup={}
            i=0,num=3,lookup={3:[0]}
            i=1,num=1,lookup={3:[0], 1:[1]}
            i=2,num=4,lookup={3:[0], 1:[1], 4:[2]}
            i=3,num=1,lookup={3:[0], 1:[1, 3], 4:[2]}
            i=4,num=5,lookup={3:[0], 1:[1, 3], 4:[2], 5:[4]}
        # second loop
            i=0,num=3,pairs={(0, 1), (0, 3)}
            i=1,num=1,pairs={(0, 1), (0, 3)}
            i=2,num=4,pairs={(0, 1), (0, 3)}
            i=3,num=1,pairs={(0, 1), (0, 3)}
            i=4,num=5,pairs={(0, 1), (0, 3)}
        """
        
        # time O(N + N) ~ O(N) 
        # space O(N + N) ~ O(N)
        # where N is size of nums list
        
        # create a set/dict
        lookup: Dict[int, List[int]] = {}
        for i, num in enumerate(nums):
            if num in lookup:
                lookup[num].append(i)
            else:
                lookup[num] = [i]
                
        # go through the num list
        pairs: Set[Tuple[int]] = set()
        for i, num in enumerate(nums):
            _val: int = None
            if num - k in lookup: 
                _val = num - k
            elif num + k in lookup:
                _val = num + k
            if _val is not None:
                for j in lookup[_val]:
                    if i == j:
                        continue
                    if not (nums[j], nums[i]) in pairs:
                        pairs.add((nums[i], nums[j]))

        return len(pairs)
                
