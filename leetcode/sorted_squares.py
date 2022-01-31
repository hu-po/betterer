class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
            Sorted in non-decreasing order
            return array of the squares of each number sorted in non-decreasing order
        """

        # inputs
        if not nums:
            return nums

        if len(nums) == 1:
            return [nums[0]**2]

        # items in nums might be negative, which means they will be at the front. when they are squared they become larger and need to get put in the back

        # brute force
        # time O(NlogN)
        # space O(N)
        
        # return sorted([n **2 for n in nums])

        """
        test cases:
        [-2, 0, 1]
        ps=0, pe=2

        [-2, 0, 3]
        ps=0, pe=2

        """

        # better solution
        # time O(N)
        # space O(1)
        # pointers at the start and end, comparing these
        ptr_s: int = 0
        ptr_e: int = len(nums) - 1

        while ptr_e > ptr_s:
            if abs(nums[ptr_e]) > abs(nums[ptr_s]):
                nums[ptr_e] = nums[ptr_e]**2
                ptr_e -= 1
            else:
                nums[ptr_s:ptr_e+1] = nums[ptr_s+1:ptr_e+1] + [nums[ptr_s] ** 2]
                ptr_s += 1
        return nums
