class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        if not len(s) % k == 0:
            s += fill * (k - len(s) % k)
            
        return [s[k*i:k*i+k] for i in range(len(s) // k)]
      
from typing import Dict

from queue import Queue, PriorityQueue
from typing import List, Set, Dict

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        # BFS
        to_explore: Queue = Queue()
        to_explore.put((1, 0, maxDoubles))
        explored: Set = set()
        
        while not to_explore.empty():
            cur, moves, doubles = to_explore.get()
            explored.add((cur, doubles))
            
            if cur == target:
                return moves
            
            if doubles > 0 and not (cur * 2, doubles - 1) in explored:
                to_explore.put((cur * 2, moves + 1, doubles - 1))
            
            if cur + 1 > 1 and not (cur + 1, doubles) in explored:
                to_explore.put((cur + 1, moves + 1, doubles))
        
        return -1
      
class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        cached: Dict = {}
        
        def take_test(question: int) -> int:
            
            if question >= len(questions):
                return 0

            if cached.get(question, None) is not None:
                return cached[question]

            points, to_skip = questions[question]
            
            if question == len(questions):
                return points

            # solve it
            solve_points = points + take_test(question + to_skip + 1)

            # skip it
            skip_points = take_test(question + 1)
            
            cached[question] = max(solve_points, skip_points)
            
            return cached[question]
        
        return take_test(0)
from queue import PriorityQueue
from typing import List, Set, Dict

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        bats: PriorityQueue = PriorityQueue()
        for battery in batteries:
            bats.put((-battery, battery))
        
        minutes: int = 0
        refill: List[Tuple[int, int]] = []
        while not bats.empty():
            refill = []
            for c in range(n):
                if bats.empty():
                    return minutes
                _, power = bats.get()
                power -= 1
                if power >= 1:
                    refill.append((-power, power))
            for bat in refill:
                bats.put(bat)
            minutes += 1
            
        return minutes
        
        
