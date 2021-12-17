class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
    
        # Space O()
        # Time O()
        
        # Edge
        # Empty matrix
        # different sized lists (rows)
        # width or height is 1
        # Matrix of size 1
        if not matrix:
            return 0
        
        y: int = len(matrix)
        x: int = len(matrix[0])
            
        if y == "1" and x == "1":
            if matrix[0][0] == "1":
                return 1
            else:
                return 0
            
        # Algo
        
        # Cast to int
        matrix: List[List[int]] = [[int(n) for n in row] for row in matrix]
        
        # Keep track of max side length
        max_side: int = 0

        # Dynamic Programming
        for yi in range(y):
            for xi in range(x):
                if yi and xi and matrix[yi][xi]:
                    matrix[yi][xi] = 1 + min(matrix[yi-1][xi], matrix[yi-1][xi-1], matrix[yi][xi-1])
                if matrix[yi][xi] > max_side:
                    max_side = matrix[yi][xi]
        
        return max_side * max_side
                      
#         for yi in range(0, y-1):
#             for xi in range(0, x-1):
#                 if matrix[yi][xi] == "0":
#                     print(f'zero ecountered at matrix[{yi}][{xi}]')
#                     break
#                 else:
#                     for yj in range(yi+1, y):
#                         for xj in range(xi+1, x):
#                             if matrix[yj][xj] == "0":
#                                 print(f'zero ecountered at matrix{yj}{xj}')
#                                 break
#                             else:
#                                 print(f'square at matrix[{yi}:{yj}][{xi}:{xj}]')
#                                 cur_area = (xj-xi)*(yj-yi)
#                                 if cur_area > max_area:
#                                     max_area = cur_area

#         # Return
#         # largest area of largest square w/ only 1
#         # start index, stop index for X and Y (4 numbers)
#         return max_area