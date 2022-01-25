class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         # brute force
#         result: List[int] = [0] * len(nums)
#         i: int = 0
#         for num in nums:
#             if not num == 0:
#                 result[i] = num
#                 i += 1
#         return result
        
        # two pointers
        last_non_zero: int = 0
        for i in range(len(nums)):
            if not nums[i] == 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1 
        return nums
        
        
        
