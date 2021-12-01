    def search(self, nums: List[int], target: int) -> int:
        lo: int = 0
        hi: int = len(nums)
        while lo < hi:
            mid: int = lo + (hi - lo)//2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                hi = mid
        return -1
