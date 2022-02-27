from typing import Set, Dict
from queue import Queue

class Solution:
    def trap(self, height: List[int]) -> int:
        
        """
        elevation map: List[int] non - negative
        how much water can it trap (areas of negative slope followed by positive slope)
        
        make this a graph problem, sort the height array (but keep track of index)
        start from lowest points, if both walls are increasing, then continue to grow "puddle" if not then save water stored and remove from list.
        
        we might have to merge puddles
        
        iteratively - moving from left to right keeping track of tallest point so far        

        """
        
        
        max_height_r: List[int] = [height[0]] * len(height)
        for i in range(1, len(height)):
            max_height_r[i] = max(height[i], max_height_r[i-1])
        
        max_height_l: List[int] = [height[-1]] * len(height)
        for i in range(len(height) - 2, 0, -1):
            max_height_l[i] = max(height[i], max_height_l[i+1])
            
        tot_water: int = 0
        for i, h in enumerate(height):
            tot_water += max(min(max_height_l[i], max_height_r[i]) - h, 0)
            
        # time O(N + N + N) ~ O(N)
        # space O(N + N + 1) ~ O(N)
         
        return tot_water
            

#         tot_water: int = 0
#         cur_water: int = 0
#         cur_height: int = 0
        
#         for x in height:
#             print(f'x {x}')
#             print(f'\t cur_height {cur_height}')
#             print(f'\t tot_water {tot_water}')
#             print(f'\t cur_water {cur_water}')
            
#             if cur_water > 0 and x > cur_height:
#                 tot_water += cur_water
#                 cur_water = 0
#                 cur_height = x
#             cur_water += cur_height - x
            
                
#         return tot_water
            
        
#         puddles: Dict[int, List[int]] = []
        
        
#         # BFS
#         visited: Set = set()
#         to_visit: Queue = Queue()
        
#         # Put all nodes into visit queue
#         for i, h in enumerate(height):
#             to_visit.put((i, i, h))
            
#         while not to_visit.empty():
#             p_s, p_e, h = to_visit.get()

#             p_s -= 1
#             p_e += 1
            
#             if p_s - 1 < 0:
#                 break
#             if p_e + 1 > len(height):
#                 break
            
            
            
#             if height[p_s - 1] < h or height[p_e + 1] < h:
#                 break
            
#             puddle_water += (p_e + 1) - (p_s - 1)
#             puddle_nodes += [,]
            
#             to_visit.put((p_s, p_e, h + 1))
