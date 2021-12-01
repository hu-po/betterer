class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        
        
        if x < 0:
            return False
        
        
        # Can you remove the center if the number of digits is odd?
        
        # Something with a queue, stack, something you can pop()
        
        # Math solution -> tricky mod bit shift
        
        x = str(x)
        l = len(x)
        if l == 1:
            return True
        if l == 2:
            if x[0] == x[1]:
                return True
            return False
        for i in range(int(l/2)):
            if not x[i] == x[-(i+1)]:
                return False
        return True

121

#         1234321
        
#         7 / 2 = 3
        
#         0, 1, 2
        
#         0 = 6
#         1 = 5
        
#         x[0] = x[6]
#         x[i] = x[len(x)-1-i]
        
#         x[1] = x[5]
#         x[i] = x[len(x)-1-i]
        
        
        
        