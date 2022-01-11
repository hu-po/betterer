        # # cheese solution
        # nums1[m:] = nums2
        # nums1[:] = sorted(nums1)
        
        # # kosher solution
        # if m == 0:
        #     nums1[:] = nums2
        #     return
        # if n == 0:
        #     return
        # sol: List[int] = [0] * (m + n)
        # i: int = 0
        # j: int = 0
        # while i < m or j < n:
        #     if not j < n:
        #         sol[i + j] = nums1[i]
        #         i += 1
        #     elif not i < m:
        #         sol[i + j] = nums2[j]
        #         j += 1
        #     elif nums1[i] <= nums2[j]:
        #         sol[i + j] = nums1[i]
        #         i += 1
        #     else:
        #         sol[i + j] = nums2[j]
        #         j += 1
        # nums1[:] = sol
        
        # better kosher solution
        i: int = m - 1
        j: int = n - 1
        k: int = m + n - 1
        while k >= 0:
            if j < 0:
                nums1[k] = nums1[i]
                i -= 1
            elif i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
