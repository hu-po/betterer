# n houses
# wells and pipes
# build a well costs wells[i - 1]
# or pipe in water from another well
# cost to build pipe is [house1, house2, cost]
# connections are bidirectional
# houses can have multiple connections

# return minimum total cost to supply water to all the houses

# graph problem -> DFS BFS

# is there one solution? yes
# pipes cost array, can we assume its good? yes
# cost can be negative? no
# have to find every path, compare which one is the smallest
# is there a pipes/well cost for every house? wells yes, pipes no

from queue import Queue
from typing import Set, Dict, Tuple

def solution(n: int, wells: List[int], pipes: List[List[int]]) -> int:

	min_cost: int = int(float.inf)

	
	# make pipes costs into dict
	pipe_cost: Dict[Tuple[int], int] = {}
	out_pipes: Dict[int, Set[int]] = {}
	for h1, h2, cost in pipes:
		if pipe_cost.get((h1, h2), None) is None:
			pipe_cost[(h1, h2)] = cost
		if pipe_cost.get((h2, h1), None) is None:
			pipe_cost[(h2, h1)] = cost
		if h1 in out_pipes and h2 not in out_pipes[h1]:
			out_pipes[h1].add(h2)
		else:
			out_pipes[h1] = Set(h2)
		if h2 in out_pipes and h1 not in out_pipes[h2]:
			out_pipes[h2].add(h1)
		else:
			out_pipes[h2] = Set(h1)

"""
	def cost(houses_w: Set[int], houses_d: Set[int]) -> cost:
# base case
if not houses:
	return 0

costs: List[int] = 0

# put a well in the house
	for house in houses_d:
		houses_w.add(house)
		houses_d.pop(house)
		cost = wells[house-1] + cost(houses_w, houses_d)
		
# for each possible pipe out in that house
for pipe_to_house in out_pipes[house]:
	houses_w.pop(pipe_to_house)
	houses_d.pop(pipe_to_house)
	pipe_cost[house, pipe_to_house] + cost(houses_w, houses_d)
	"""
# cost to put well in every house
# go through the pipe cost array, add one pipe at a time (remove that house)
# keep track of a global minimum

to_explore : Queue = Queue()

wet : List[int] = [i for i in range(houses)]
dry : List[int] = []
cost: int = [wells[i] for i in range(houses)]
to_explore.put((cost, wet, dry))
	
	while not to_explore.empty()
		cost, wet, dry = to_explore.get()
		if not dry:
			min_cost = min(min_cost, cost)
		for wh in wet:
			
		

return min_cost
