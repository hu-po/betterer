class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        # Check if X intersects
        if (rec2[0] < rec1[0] < rec2[2]) or \
           (rec2[0] < rec1[2] < rec2[2]) or \
           (rec1[0] < rec2[0] < rec1[2]) or \
           (rec1[0] < rec2[2] < rec1[2]):
            pass
        else:
            return False
        
        # Check if Y intersects
        if (rec2[1] < rec1[1] < rec2[3]) or \
           (rec2[1] < rec1[3] < rec2[3]) or \
           (rec1[1] < rec2[1] < rec1[3]) or \
           (rec1[1] < rec2[3] < rec1[3]):
            return True
        else:
            return False
