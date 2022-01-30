from typing import Set
from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # inputs, edge cases, etc
        if not root or not target:
            return []
        
        if k == 0:
            return [target.val]

        # array of node values that have distance k from target node
        # any order
        node_vals_in_k : List[int] = []
        
        # acyclic graph?
        # is list of node values unique?
                
        # DFS: Add a parent property to every node
        visited: Set = set()
        to_visit: Queue = Queue()
        to_visit.put((None, root))
        while not to_visit.empty():
            parent, node = to_visit.get()
            node.parent = parent
            for nnode in [node.left, node.right]:
                if nnode is None:
                    continue
                if nnode not in visited:
                    to_visit.put((node, nnode))
                    visited.add(nnode)
        
        # BFS: expand out from target node
        visited: Set = set()
        to_visit: Queue = Queue()
        to_visit.put((0, target))
        d : int = 0
        while not to_visit.empty():
            d, node = to_visit.get()
            if d == k:
                node_vals_in_k.append(node.val)
            if d > k:
                break
            visited.add(node)
            for nnode in [node.left, node.right, node.parent]:
                if nnode is None:
                    continue
                if nnode not in visited:
                    to_visit.put((d + 1, nnode))
                    visited.add(nnode)
                    
        # time.O(N + N) ~ O(N)
        # space.O(N + N + M) ~ O(N)
        # where N is number of nodes in tree
        # where M is number of nodes k away from target
        
        return node_vals_in_k
