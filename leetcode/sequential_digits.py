import math
from typing import Set, List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        # sequential if digitN+1 = digitN + 1
        # return sorted list of integers in [low, high]
        
        # [100, 3500] -> [123, 234]
        
        # Go down the number of powers of 10
        # for each power of 10, get the allowed sub-powers of 10
        # recursion/memoization?
        
        # bad inputs
        if not high or not low or high <= low:
            return []
        
#         # next digit
#         next_digit: int = digit + 1
#         if next_digit >= 10:
#             return None
        
#         # Cache all answers for all powers of 10 up to the high mark
#         all_sequential_digits: Dict = {
#             1: 1,
#             2: [12, 23, 34, 45, 56, 67, 78, 89],
#         }
            
#         def next_powten(digit: int, powten: int) -> int:
#             if powten == 0:
#                 return 0
#             if powten == 1:
#                 return digit
            
#             if pow10 in all_sequential_digits.keys():
#                 yield all_sequential_digits[pow10]
            
#             for _next_powten in next_powten(digit + 1, powten - 1)
            
#                 return (10**powten) * digit + 
        
#         # Populate all sequential digits up until high mark
#         for powten in range(0, int(math.log10(high))):
#             for digit in range(1, 9):
#                 if (10**powten) * digit > high:
#                     break
                
#         return sequential_digits

        # Looked at answer, string slicing is answer
    
        # M = powH - powL
        # N = final length of numseq
        # Time O(1 + 1 + 1 + M * ((10 - M) * (10 - M)) + 1) + NlogN) ~ O(M**3 + NlogN)
        # Space O(1 + 1 + N) ~ O(N)
        
        min_pow10 = int(math.log10(low))
        max_pow10 = int(math.log10(high))
        
        sequential_nums: List[int] = []
        
        for num_digits in range(min_pow10 + 1, max_pow10 + 2):
            for start in range(10 - num_digits):
                num: int = 0
                for digit in range(start, start + num_digits):
                    if num > high:
                        break
                    num = 10 * num + (digit + 1)
                if low <= num <= high:
                    sequential_nums.append(num)
        
        # This isn't actually needed since list is already sorted
        sequential_nums.sort()
        return sequential_nums

        
        
