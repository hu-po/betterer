from queue import Queue
from typing import Set

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        from i you can jump to i + arr[i] or i-arr[i]
        return true if you can reach any index with value 0
        
        graph problem w/ first valid solution works, check all solutions - BFS
        
        """
        
        # check inputs and edge cases
        if not arr:
            return False
        
        if arr[start] == 0:
            return True
        
        if len(arr) == 1:
            return False
        
        # TODO: check for improperly formatted inputs
        
        def get_neighbors(x: int) -> int:
            """ Yield neighboring nodes given a node."""
            if 0 <= x + arr[x] < len(arr):
                yield x + arr[x]
            if 0 <= x - arr[x] < len(arr):
                yield x - arr[x]
        
        # bfs
        visited: Set = set()
        to_visit: Queue = Queue()    
        to_visit.put(start)
        visited.add(start)
        while not to_visit.empty():
            node = to_visit.get()
            if arr[node] == 0:
                return True
            for nnode in get_neighbors(node):
                if not nnode in visited:
                    if arr[node] == 0:
                        return True
                    to_visit.put(nnode)
                    visited.add(nnode)
                    
                    
        # time O(1 + 1 + N) ~ O(N)
        # space O(1 + N + N) ~ O(N)
        # where N is length of list

        return False
