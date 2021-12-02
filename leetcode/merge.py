class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Using built-ins
        # nums1[:] = sorted(nums1[:m] + nums2)
        

        
        # O(N)
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return
        
        p1 = m - 1
        p2 = n - 1
        
        for i in range(m + n - 1, -1, -1):
            if p2 < 0:
                nums1[i] = nums1[p1]
                p1 -= 1
                continue
            if p1 < 0:
                nums1[i] = nums2[p2]
                p2 -= 1
                continue

            if nums1[p1] < nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1