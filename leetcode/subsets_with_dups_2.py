from typing import Set

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        """
        nums: List[int] - may contain duplicates
        return all possible subsets in any order
        """
        
        # check inputs and edge cases
        if not nums:
            return [[]]
        
        # time O(N*(N)) ~ O(N!)
        # space O(N!) ~ O(N!) where N is length of N
        
        possible_subsets: Set[List[ints]] = set()
        for i in range(0, len(nums)+1):
            for subset in itertools.combinations(nums, i):
                possible_subsets.add(tuple(sorted(list(subset))))
        return list(possible_subsets)
