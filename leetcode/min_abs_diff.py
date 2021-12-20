class Solution:    
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        # arr: List[int] -> List[Tuple[int, int]]

        # all pairs of elements min(abs(a, b))
        # list of pairs
        # a < b
        # b - a = min_absolute_diff
        
        # Space O(2*N + C) ~ O(N)
        # Time O(C + NlogN + NlogN)) ~ O(NlogN)
        
        # edge cases
        # empty list
        # numbers not ints
        # list of length 1
        if not arr or len(arr) < 2:
            return None
        
        # algo
        pairs: List[Tuple[int]] = []
        min_abs_diff: int = float('inf')
        a: int = 0
        b: int = 0
        
        # sort the list O(NlogN)
        arr = sorted(arr)
        
        # Starting from bottom 
        for i, a in enumerate(arr):
            # print(f'a {a}, i {i}')
            for j in range(i+1, len(arr)):
                b = arr[j]
                # print(f'b {b}, j {j}')
                abs_diff: int = abs(b - a)
                if abs_diff > min_abs_diff:
                    break
                elif abs_diff <= min_abs_diff:
                    if abs_diff < min_abs_diff:
                        min_abs_diff = abs_diff
                        pairs = []
                    pairs.append((a, b))
                    # print(f'pairs {pairs}')
                    

        # return
        return pairs
    
# [4, 2, 1]
# [1, 2, 4]
# i=0, a=1
#     j in 0 to 3
#     j=1, b=2, abs_diff=1, min_abs_diff=1, pairs[(1, 2)]
#     j=2, b=4, abs_diff=3, break
# i=1, a=2
#     j in 1 to 3
#     j=2, b=4, abs_diff=2, break
# i=2, a=4
#     j in 2 to 3, break
