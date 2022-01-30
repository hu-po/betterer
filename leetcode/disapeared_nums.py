class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # integers nums len(nums) == n, 1 < nums[i] < n
        # return array of integers in range [1, n] that do not appear in nums
        
        
        # time.O(N)
        # space.O(M + N) - where M is unseen ints
        unseen_nums : List[int] = []
        unique_nums: Set = set(nums)    
        for i in range(1, len(nums)+1):
            if not i in unique_nums:
                unseen_nums.append(i)
        return unseen_nums
    
#         # time.O(N + NlogN)
#         # space.O(M)
        
#         """
#         [4, 2, 2, 3]
#         [2, 2, 3, 4]
#         ptr=0
#             i=1, ptr=1, un=[1]
#             i=2,
#             i=3,
        
#         """
        
#         nums = sorted(nums)
#         unseen_nums : List[int] = []
#         ptr: int = 0
#         for i in range(1, len(nums)+1):
#             if ptr == len(nums):
#                 break
#             if nums[ptr] == i:
#                 ptr += 1
#                 continue
#             if nums[ptr] > i:
#                 ptr += 1
#             unseen_nums.append(i)
#         return unseen_nums
