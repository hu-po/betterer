from typing import Dict, Set
from queue import PriorityQueue

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # tree of n nodes labeled (0, n-1)
        # array of (n-1) edges edges[i] = (ai, bi) undirected edges
        # root is any node, h is height of tree, find min(h)
        # return ALL of the min(h) roots in any order
        # height needs to be at least 1 (no leaf nodes)
        
        # Space O()
        # Time O()
        
        # Edge cases
        # No nodes, empty nodes, no edges, empty edges'
        # Un-connected nodes?
        # Edge loops
        if not edges or n <= 1:
            return [0]
        
        # Algo
        # DFS or BFS
        min_heights: Dict[int : int] = {n : 0 for n in range(n)}
        
        # Build a dictionary of each node's connections
        connections: Dict[int : Set] = {n : set() for n in range(n)}
        for na, nb in edges:
            connections[na].add(nb)
            connections[nb].add(na)
        # print(f'connections {connections}')
        
        leaves = [n for n, nodes in connections.items() if len(nodes) == 1]
        
        while n > 2:
            n -= len(leaves)
            tmp = []
            for leaf in leaves:
                neighbor = connections[leaf].pop()
                connections[neighbor].remove(leaf)
                if len(connections[neighbor]) == 1:
                    tmp.append(neighbor)
            leaves = tmp
        return leaves
                                
#         # Add all edges to PriorityQueue
#         for n, nodes in connections.items():
            
#             # There are connecting nodes
#             if nodes:
                
#                 # Keep track of exploration depth for this node
#                 depth: int = 1
#                 min_heights[n] = depth
                
#                 # Create a BFS queue of connecting nodes
#                 to_explore: PriorityQueue = PriorityQueue()
#                 for node in nodes:
#                     if not node == n:
#                         to_explore.put((depth, node))
                        
#                 # Find the minimum depth connecting node
#                 while not to_explore.empty():
#                     depth, node = to_explore.get()
#                     # print(f'exploring {node} at depth {depth}')
                    
#                     if depth > min_heights[n]:
#                         min_heights[n] = depth
                        

#                     else:
#                         for node_i in connections[node]:
#                             if not node == node_i:
#                                 to_explore.put((depth+1, node_i))
                            
                        
#         print(f'min_heights {min_heights}')
        
# #         # Recursion
        
# #         # Bi-directional edge adds length 1 to both nodes
# #         for na, nb in edges:
# #             if height.get(na, None) is None:
# #                 height[na] = 1
# #             else:
# #                 height[na] += 1
# #             if height.get(nb, None) is None:
# #                 height[nb] = 1
# #             else:
# #                 height[nb] += 1
        
#         # Return
#         return [n for n, h in min_heights.items() if h == min(min_heights.values())]
        