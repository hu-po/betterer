class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return None
        

        # space.O(N)
        # time.O(N)
        
        nums_diff: List[int] = [target - n for n in nums]

        for i, num in enumerate(nums):
            if num in nums_diff:
                idx: int = nums_diff.index(num)
                if not idx == i:
                    return [i, idx]
        return None
