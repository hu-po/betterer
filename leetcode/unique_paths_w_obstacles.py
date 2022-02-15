from queue import Queue
from typing import Set

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        grid: List[List[int]]
        robot can move down or right
        robot wants to reach bottom-right corner of the grid
        obstacles in path (1s in grid)
        return number of unique paths
        
        graph problem
        bfs
        
        can there be zero paths? obstacles blocking robot or goal?
        
        test cases:
            [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,0]]
            [[0,0,0],[0,1,0],[0,0,0]]
            [[0,0,0,0],[0,1,0,1],[0,0,0,0]]
            [[0,0],[0,1]]
            [[1,0],[0,1]]
            [[0]]
            [[0, 0, 0, 1, 0]]
            [[0],[0],[0]]
            [[0],[1],[0]]
            [[0,1],[0,0]]
            [[0,0],[1,1],[0,0]]
        """
        
        # check inputs and edge cases
        if not obstacleGrid:
            return 0
        
        h: int = len(obstacleGrid)
        w: int = len(obstacleGrid[0])
        
        # goal/robot is obstacle
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0
        
        # grid is straight path
        if w == 1:
            if any([r[0] for r in obstacleGrid]):
                return 0
            else:
                return 1
        if h == 1:
            if any(obstacleGrid[0]):
                return 0
            else:
                return 1
        
        # obstacle blocking robot
        if obstacleGrid[0][1] and obstacleGrid[1][0]:
            return 0
        
        # obstacle blocking goal
        if obstacleGrid[-1][-2] and obstacleGrid[-2][-1]:
            return 0
        
        def get_neighbors(y: int, x: int) -> Tuple[int]:
            """ robot can only move down or right. """
            for yn, xn in [(y+1, x),(y, x+1)]:
                if yn >= h:
                    continue
                if xn >= w:
                    continue
                if obstacleGrid[yn][xn]:
                    continue
                yield yn, xn
        
        # total unique paths
        num_paths: int = 0
        goal_reached: bool = False
        
        # dfs
        visited: Set[Tuple[int]] = set()
        to_visit: Queue = Queue()
        to_visit.put((0, 0)) # h, w
        while not to_visit.empty():
            y, x = to_visit.get()
            visited.add((y,x))
            # print(f'visiting {(y, x)}')
            if (y == h-1) and (x == w-1):
                goal_reached = True
            for yn, xn in get_neighbors(y, x):
                if not (yn, xn) in visited:
                    visited.add((yn,xn))
                    to_visit.put((yn,xn))
                else:
                    num_paths += 1
        
        return num_paths if goal_reached else 0
