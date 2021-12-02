class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) < 2:
            raise ValueError
        
        # # O(N*N) - M(-)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (nums[i] + nums[j]) == target and not i == j:
        #             return [i, j]
                
        # O(N + N) - M(N)
        target_hash = {target - num : i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            j = target_hash.get(num, None)
            if j is not None and not j == i:
                return [i, j]