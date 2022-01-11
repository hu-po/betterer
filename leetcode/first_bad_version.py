    def firstBadVersion(self, n) -> int:
        """
        :type n: int
        :rtype: int
        """
        # Time O(NlogN)
        # Space O(1)
        hi: int = n
        lo: int = 1
        while lo < hi:
            mid: int = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
