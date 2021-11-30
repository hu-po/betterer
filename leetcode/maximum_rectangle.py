from typing import List
import numpy as np

class Solution:


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        # Convert to numpy for easier time
        matrix = np.array(matrix, dtype=int).astype(bool)
        
        # Edge cases
        max_size = 1
        if not np.any(matrix):
            # All zeros
            return 0
        
        # Get the height matrix
        h_matrix = np.zeros(matrix.shape, dtype=int)
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):  
                if matrix[x, y]:
                    h_matrix[x, y] = h_matrix[x-1, y] + 1
                else:
                    h_matrix[x, y] = 0

        print(h_matrix)

        # Find the most consecutive same numbers
        for x in range(matrix.shape[0]):
            size = h_matrix[x, 0]
            height = size
            consecutive = 1
            for y in range(1, matrix.shape[1]):  
                if h_matrix[x, y] > 0:
                    consecutive += 1
                    height = min(h_matrix[x, y], height)
                    size = height * consecutive
                else:
                    consecutive = 1
                    size = h_matrix[x, y]
                    height = size

                if size > max_size:
                    max_size = size

        return max_size

    def rec_size(self, xa: int, ya: int, xb: int, yb: int) -> int:
        return (yb - ya) * (xb - xa)
    
    def check(self, matrix: np.ndarray, x: int, y: int, xb: int, yb: int):
    
        in_bounds = (xb < matrix.shape[0] and yb < matrix.shape[1])
        check_both = np.all(matrix[x:xb+1,y:yb+1])
        
        if in_bounds and check_both:
            return self.check(matrix, x, y, xb+1, yb+1)
        
        if (yb < matrix.shape[1] and np.all(matrix[x:xb,y:yb+1])):
            return self.check(matrix, x, y, xb, yb+1)

        if (xb < matrix.shape[0] and np.all(matrix[x:xb+1,y:yb])):
            return self.check(matrix, x, y, xb+1, yb)
        
        return matrix, x, y, xb, yb

            
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        # Convert to numpy for easier time
        matrix = np.array(matrix, dtype=int).astype(bool)
        
        # Edge cases
        max_max_size = 0
        if np.any(matrix):
            # At least one one
            max_max_size = 1
        else:
            # All zeros
            return max_max_size
        
        x = 0
        while x < matrix.shape[0]:
            y = 0
            while y < matrix.shape[1]:
                
                _, xa, ya, xb, yb = self.check(matrix, x, y, x, y)

                max_size = self.rec_size(xa, ya, xb, yb)
                if max_size >= max_max_size:
                    max_max_size = max_size

                y += 1
            x += 1
            
        return max_max_size


print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(Solution().maximalRectangle([["0","1"],["0","1"]]))
print(Solution().maximalRectangle([["1","0"],["1","0"]]))
print(Solution().maximalRectangle([["0","0","1"],["1","1","1"]]))