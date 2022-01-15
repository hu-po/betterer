from queue import Queue
from typing import Dict, Set

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        start_i: int = 0
            
        # step forward or backwards (i+1) and (i-1)
        # jump to same values arr[i] == arr[j]
        #  min num of steps
        
        # Graph search problem, fastest path. DFS or BFS
        # we want global minimum, so we will have to go through all the nodes
        
        # argument edge cases
        if not arr or len(arr) <= 1:
            return 0
        
        # return the minimum number of jumps required=
        min_jumps: int = 0
            
        # build the graph: a dict with node connections for each node
        # TODO: Find better than O(N**2)
        graph: Dict[int, Set[int]] = {}
        for node in range(len(arr)):
            if graph.get(arr[node], None) is not None:
                graph[arr[node]].add(node)
            else:
                graph[arr[node]] = {node}

        # BFS
        to_explore: Queue = Queue()
        to_explore.put((0, 0))
        explored: Set = set()
        
        while not to_explore.empty():
            min_jumps, node = to_explore.get()
            
            # Get to the end in BFS is the minimum path
            if node == len(arr) - 1:
                return min_jumps
            
            # Check hyper jumps
            for _node in graph[arr[node]]:
                if not _node in explored:
                    to_explore.put((min_jumps + 1, _node))
                    explored.add(node)

            # Get rid of hyperjumps to prevent cycles
            graph[arr[node]].clear()
            
            # take a forward step
            forward: int = node + 1
            if forward <= len(arr) and not forward in explored:
                to_explore.put((min_jumps + 1, forward))
                explored.add(forward)
                
            # take a backwards step
            backward: int = node - 1
            if backward >= 0 and not backward in explored:
                to_explore.put((min_jumps + 1, backward))
                explored.add(backward)

        
        
