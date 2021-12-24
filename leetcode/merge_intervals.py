from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
        # overlapping intervals
        # intervals improperly formatted?
        
        if not intervals:
            return None
        
        # Negative numbers? negative intervals?
        # Are these sorted?
        # Could we sort them based on the first number?
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # [[1,3],[2,6],[8,10],[15,18]]
        # [[1,6],[8,10],[15,18]]
        
        # Space O()
        # Time O(NlogN + )
        
        # Brute force: for each interval, check all other intervals
        # In-place? Or do we need to make a new list of valid intervals to return?
        merged: List[List[int]] = []
        
       # Go through each interval
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            elif merged[-1][1] < end:
                merged[-1][1] = end
        return merged
