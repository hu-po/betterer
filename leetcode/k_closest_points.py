import math
from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # edge cases
        # k is zero, k is negative, k is None'
        # points is empty, points is None, points misformatted (different lengths)
        # k is larger than number of points?
        
        if not points or k < 1:
            return None
        
        if len(points) < k:
            return points
        
        # sorted? will sorting make this easier?
        # k closest points to origin
        
        # Space O(N + N) ~ O(N)
        # Time O(N + N) ~ O(N)
        
        # priority queue? priority is distance
        closest_points: PriorityQueue = PriorityQueue()
        for x, y in points:
            closest_points.put((
                math.sqrt(x**2 + y**2), # distance
                (x, y) # point
            ))
        
        # in place
        points: List = []
        for _ in range(k):
            _, point = closest_points.get()
            points.append(point)
            
        return points
      
      # One liner
        points.sort(key = lambda x: math.sqrt(x[0]**2 + x[1]**2))
        return points[:k]
            
        
