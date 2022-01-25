class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
    
        # for each element in nums1, find corresponding element of nums2
        # for this element find next greater element, -1 if no element
        
#         # bad inputs
#         if not nums1 or not nums2:
#             return []
        
#         # set or dictionary for quick checking of location in nums2
#         nums2_dict: Dict[int, int] = {num : index for index, num in enumerate(nums2)}
            
#         # greater element might end up being the same for many of the items.
#         for i in range(len(nums1)):
#             greater_found: bool = False
#             for j in range(nums2_dict[nums1[i]] + 1, len(nums2)):
#                 if nums2[j] > nums1[i]:
#                     nums1[i] = nums2[j]
#                     greater_found = True
#                     break
#             if not greater_found:
#                 nums1[i] = -1
#         return nums1
    
    
    
        """
        
        [1, 7], [1, 5, 7, 6] -> [7, -1]
            
        N = len(nums1), M = len(nums2)
        Time O(M + N *(M - N)) ~ O(N*M)
        Space O(M + N) ~ O(M)
        
        """
        
        # Solution that is O(M) and O(M)
        stack: List[int] = []
        next_greatest_map: Dict[int : int] = {num2 : -1 for num2 in nums2}
        
        for i, num2 in enumerate(nums2):
            while len(stack) > 0:
                if stack[-1] < num2:
                    next_greatest_map[stack[-1]] = num2
                    stack.pop()
                else:
                    break
            stack.append(num2)
                        
                
        return [next_greatest_map[num1] for num1 in nums1]                
            
            
        
                    
