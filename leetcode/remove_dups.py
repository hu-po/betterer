class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # sorted non-decreasing
        
        # remove duplicates in-place
        
        # bad inputs
        if not nums:
            return 0
        
        # toy case
        if len(nums) == 1:
            return nums[0]
        
        """
        [1, 2, 2, 3]
        
        """
        
        # time.O(1 + 1 + N) ~ O(N)
        # space.O(1 + 1) ~ O(1)
        
        i: int = 0
        dup_count: int = 0
        while i + dup_count < len(nums):
            while i + dup_count + 1 < len(nums) and nums[i + dup_count] == nums[i + dup_count + 1]:
                dup_count += 1
            nums[i] = nums[i + dup_count]
            i += 1
            
        return len(nums) - dup_count
            
