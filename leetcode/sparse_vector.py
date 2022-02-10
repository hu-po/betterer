class SparseVector:
    def __init__(self, nums: List[int]):
        # lots of zeros, so only keep track of non-zeros
        self.idx_nums : Dict[int, int] = {}
        self.nonzero_count: int = 0
        for i, num in enumerate(nums):
            if not num == 0:
                self.idx_nums[i] = num
                self.nonzero_count += 1
            
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        """
            Dot product is summation of elementwise multiplication
            <x1, y1, z1> dot <x2, y2, z2> = x1*x2 + y1*y2 + z1*z2
            
            in a sparse vector, most of the time you multiply by zero so not worth calculating
        """
        answer: int = 0
        if self.nonzero_count > vec.nonzero_count:
            for idx, num in self.idx_nums.items():
                if idx in vec.idx_nums:
                    answer += num * vec.idx_nums[idx]
        else:
            for idx, num in vec.idx_nums.items():
                if idx in self.idx_nums:
                    answer += num * self.idx_nums[idx]
        return answer

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
