from queue import Queue
from typing import Dict, Set

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        """
            lock with 4 wheels
            each wheel has 10 slots (zero indexed ints)
            9 connects to 0
            one move is turning one wheel one slot
            
            given list of deadends (nodes with no outgoing edges)
            given target return minimum total number of turns
            starting node is '0000'
            
            graph problem
            we want to find the "shortest" solution (BFS)
            
            can we assume properly formatted deadends and target?
            - correct length (4 chars), all characters between 0 and 9
            
            if there is no solution, return -1
            
            "0009"
            
        """
        
        # check inputs and edge cases
        
        # convert target and deadends to nicer datatypes
        deadends : Set = set(deadends)
            
        if "0000" in deadends:
            return -1                
                
        def get_neighbors(combo: str) -> str:
            """ Yield possible next combos given a single turn on a single wheel. """
            for i, char in enumerate(combo):
                pre: str = combo[:i] if i > 0 else '' 
                suf: str = combo[i+1:] if i < 3 else ''
                if char == '9':
                    yield f'{pre}8{suf}'
                    yield f'{pre}0{suf}'
                elif char == '0':
                    yield f'{pre}9{suf}'
                    yield f'{pre}1{suf}'
                else:
                    yield f'{pre}{str(int(char) + 1)}{suf}'
                    yield f'{pre}{str(int(char) - 1)}{suf}'
        
        # A-star search
        visited: Set = set()
        to_visit: Queue = Queue()
        
        # start at 0-0-0-0 (turns, combo)
        to_visit.put((0, "0000"))
        
        while not to_visit.empty():
            turns, combo = to_visit.get()
            visited.add(combo)
            if combo == target:
                return turns
            if combo in deadends:
                continue
            for n_combo in get_neighbors(combo):
                if (not n_combo in deadends) and (not n_combo in visited):
                    visited.add(n_combo)
                    to_visit.put((turns+1, n_combo))
                    
                    
        # time O(N*M) 
        # space O(1 + N*M)
        # where N is length of path from start to target node and M is width of tree
                
        return -1
