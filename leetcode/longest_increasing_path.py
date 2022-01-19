from queue import LifoQueue
from typing import List, Tuple, Set, Dict

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0
        
        # check inputs
        width: int = len(matrix[0])
        height: int = len(matrix)

        if width <= 1 and height <= 1:
            return 1
        
        if not width or not height:
            return 0

        # Graph search (DFS/BFS)
        
        def get_neighbors(x: int, y: int) -> Tuple[int, int]:
            """
            4-point connectivity
            directed edges from nodeA <= nodeB
            """
            for xn, yn in [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
            ]:
                if xn < 0 or yn < 0 or xn >= width or yn >= height:
                    continue
                if matrix[yn][xn] < matrix[y][x]:
                    yield (xn, yn)
        
        # Visitation graph {(x, y) : max_len}
        explored: Dict[Tuple[int, int], int] = {}
        
        # DFS - LifoQueue
        to_explore: LifoQueue = LifoQueue()
        
        # Add all the nodes the exploration queue
        for x in range(width):
            for y in range(height):
                to_explore.put(((x, y), 1))
                explored[(x, y)] = 1
        
        while not to_explore.empty():
            node, path_len = to_explore.get()
            if path_len < explored[node]:
                continue
            for node in get_neighbors(node[0], node[1]):
                if explored[node] < path_len + 1:
                    to_explore.put((node, path_len + 1))
                    explored[node] = path_len + 1
        
        # Find the max path length
        max_len: int = 0
        for path_len in explored.values():
            max_len = max(max_len, path_len)
        
        # Return length of maximum path
        return max_len
