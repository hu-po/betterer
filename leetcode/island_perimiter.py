from typing import Set, Dict
from queue import Queue, LifoQueue, PriorityQueue

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        """
        grid: List[List[int]] - 
        1 is land, 0 is water
        4 way connectivity (up/down)
        exactly 1 island
        no lakes, each grid square is of dimmension 1x1
        what is perimiter of island?
        
        graph problem, BFS/DFS/A*
        
        [
        [0, 0, 0],
        [0, 0, 1],
        ]
        
        """
        
        # check inputs and edge cases
        if not grid:
            return 0
        
        # width and height of grid
        h: int = len(grid)
        w: int = len(grid[0])
        
        def get_neighbors(x: int, y: int) -> Tuple[int]:
            for xn, yn in [
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1),
            ]:
                if xn < 0 or xn >= w:
                    continue
                if yn < 0 or yn >= h:
                    continue
                yield xn, yn, grid[yn][xn]
        
        # visited > { (grid x, grid y) : shoreline}
        visited: Dict[Tuple[int], int] = {}
        to_visit: Queue = Queue()
        to_visit.put((0,0,grid[0][0]))
        exploring_on_land: bool = False
        while not to_visit.empty():
            x, y, is_land = to_visit.get()
            if is_land:
                exploring_on_land = True
            # what is the shoreline?
            # 0 connected_land = 0 units of shoreline: its water!
            # 1 connected_land = 3 units of shoreline
            # 2 connected_lands = 2 unites of shoreline
            # 3 connected_lands = 1 unites of shoreline
            # 4 connected_lands = 0 unites of shoreline
            num_connected_lands: int = 0
            for xn, yn, is_landn in get_neighbors(x, y):
                if not (xn, yn) in visited:
                    if exploring_on_land:
                        if is_landn:
                            to_visit.put((xn, yn, is_landn))    
                    else:
                        to_visit.put((xn, yn, is_landn))
                if is_landn:
                    num_connected_lands += 1
            
            # Add to visitation set
            if is_land == 0:
                visited[(x,y)] = 0
            else:
                visited[(x,y)] = 4 - num_connected_lands
                
        # time O(M*N)
        # space O(M*N)
        # where grid is size MxN
            
        # print(visited)
        return sum(visited.values())
