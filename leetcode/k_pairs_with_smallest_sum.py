class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        nums1: List[int] 
        nums2: List[int]
        k: int
        
        both sorted in ascending order
        
        define (u, v) where u and v are elements from nums1 and nums2
        return the k pairs (u1, v1), (uk, vk) with the smallest sums
        
        two-pointer problem? 
        
        can there be negative numbers? yes
        can numbers be re-used? yes
        can k exceed maximum lenght of possible pairs? yes
            
            
        test cases:
        nums1=[1, 3], nums2=[2], k=3
        p1=0,p2=0,k=3,pairs=[[1,2]]
            p1=1,pairs=[[1,2],[3,2]]
        return [[1,2],[3,2]]
        
        """
        
        # check inputs and edge cases
        
        if not nums1 or not nums2:
            return []
        
        if k == 0:
            return []
        
        if k == 1:
            return [[nums1[0], nums2[0]]]
        
        # two pointer solution
        p1: int = 0
        p2: int = 0
        pairs: Set[Tuple[int]] = {(p1, p2)}
        while len(pairs) < k or len(pairs) < len(nums1)*len(nums2):    
            if p1 == len(nums1) - 1:
                p2 += 1
                if p1 >= len(nums1)-1 and p2 >= len(nums2)-1:
                    break
                else:
                    p1 = 0
            elif p2 == len(nums2) - 1:
                p1 += 1
                if p1 >= len(nums1)-1 and p2 >= len(nums2)-1:
                    break
                else:
                    p2 = 0
            elif nums1[p1] < nums2[p2]:
                p2 += 1
                if p1 >= len(nums1)-1 and p2 >= len(nums2)-1:
                    break
                else:
                    p1 = 0
            else:
                p1 += 1
                if p1 >= len(nums1)-1 and p2 >= len(nums2)-1:
                    break
                else:
                    p2 = 0
            pairs.add((p1, p2))
            
        # time O(1 + N*M) ~ O(N*M)
        # space O(1 + N*M) ~ O(N*M)
        # > where N is length of nums1
        # > where M is length of nums2
        
        return [[nums1[p1], nums2[p2]] for p1, p2 in pairs]
