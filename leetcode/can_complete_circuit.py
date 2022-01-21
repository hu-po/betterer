class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # N gas stations gas[i] is int number of gas
        # car with unlimited gas tank
        # cost[i] is travel from ith gas station to i+1 gas station
        # begin the the journey empty at one gas station
        
        # return starting gas station index if you can travel once in circuit in clockwise direction
        # else return -1
        
        # solution is guaranteed to be unique
        
        
        # bad inputs
        if not gas or not cost:
            return -1
        if not len(gas) == len(cost):
            return -1
        
        # brute force O(N^2)
        # for start_index, start_station in enumerate(gas):
            
            # loop back (once you get to len() go to start_index)
        
            # travel forward from that start index
            
                # accumulate gas[i], subtract cost[i]
                
                # if gas ever goes negative, break out
        
        # gas [1, 3, 1] cost [1, 2, 1]
        # start at 0 -> 1 - 1 + 3 - 2 (gas gained from i - cost to travel from i to i + 1)
        
        # double pointer? lookahead, current?
        
        # Time O(1 + 1 + 1 + N * (1 + 1 + 1 + 1)) ~ O(N)
        # Space O(1 + 1 + 1) ~ O(1)
        
        accum_gas: int = 0
        total_gas: int = 0
        start_idx: int = 0
        for i in range(len(gas)):
            accum_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            if accum_gas < 0:
                start_idx = i + 1
                accum_gas = 0
                
        # no matter where you start there isn't enough gas in all the stations
        # to complete a full clockwise turn
        if total_gas < 0:
            return -1
        
        return start_idx
        
