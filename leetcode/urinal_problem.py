from typing import Iterable 

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        # at least one empty seat
        # at least one person sitting
        
        # sit in the seat such that distance is maximized (urinal problem)
        
        # # brute force?
        # for seat in seats:
        #     # expand forwards and backwards
        #     # keep track of seat with maximum forwards & backwards score
                    
        # split search (cut the seats in the middle, look left, look right, etc)
        
        # Time O(N *(1 + 1 + 1 + 1)) ~ O(N)
        # Space O(1 + 1) ~ O(1)
        
#         # add up the seats? some kind of running average from left and right
#         suc_empty: int = 0
#         max_suc_empty: int = 0
#         max_suc_empty_idx: int = 0
#         nobody_at_start: bool = True
#         for i in range(len(seats)):
#             if not seats[i]:
#                 suc_empty += 1
#             if seats[i]:
#                 suc_empty = 0
#                 nobody_at_start = False
#             seats[i] = suc_empty
#             if suc_empty >= max_suc_empty:
#                 max_suc_empty = suc_empty
#                 if nobody_at_start:
#                     max_suc_empty_idx = 0    
#                 else:
#                     max_suc_empty_idx = i
            
#         if max_suc_empty_idx == 0 or max_suc_empty_idx == (len(seats) - 1):
#             return max_suc_empty
#         else:
#             return (max_suc_empty + 1) // 2

        closest_person: int = 0
        max_distance: int = 0
        
        people: Iterable[int] = (i for i, seat in enumerate(seats) if seat)
        
        prev_person: int = None
        next_person: int = next(people, None)
            
        for i, seat in enumerate(seats):
            if seat:
                prev_person = i
            if next_person is not None and i >= next_person:
                next_person = next(people, None)
            
            if prev_person is None:
                if next_person is not None:
                    closest_person = next_person - i
            elif next_person is None:
                closest_person = i - prev_person
            else:
                closest_person = min(i - prev_person, next_person - i)
                
            max_distance = max(max_distance, closest_person)
            
        return max_distance
