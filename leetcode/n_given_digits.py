from typing import Set

class Solution:
    
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        # Space O(4 + 1 + ) ~ O(1)
        # Time O(lenN + lenN*(lenD + 1 + 1 + 1)) ~ O(N*D)
        
        # Edge cases
        # n is zero or negative
        # digits is empty or len 1
        if not digits:
            return 0
        
        # Algo
        # Set (unique integers)
        # digits is strings, but to compare need ints
        # digits is sorted in ascending order
        # Starting at 1s place and going up each order of magnitude
        # If you check the largest and smallest value for each order of magnitude
        # you can probably binary search the stopping point        
        count: int = 0
        num_digits: int = len(digits)
        n: str = str(n)
        num_digits_in_n: int = len(n)
            
        # Count numbers with less digits than n
        # All less than n
        # (permutations) 3C1 + 3C2 + 3C4
        # 3 + 3 * 2 + 3 * 2 * 1 == 3^1 + 3^2 + 3^3
        for i in range(1, num_digits_in_n):
            count +=  num_digits ** i
        
        # Count numbers with same digits as n
        # Some less than n
        # Recursive binary searches for each digit place
        
        
        # Go through each digits place in N
        for i in range(num_digits_in_n):
            tmp_count: int = 0 
            # Get number of digits less than current digits place
            for d in digits:
                if d < n[i]:
                    tmp_count += 1
                else:
                    break
            count += tmp_count * (num_digits ** (num_digits_in_n - i - 1))
            # 
            if n[i] not in digits:
                break
            #
            if i == num_digits_in_n - 1:
                count += 1
        
        return count
        
#         cur_digit: int = num_digits_in_n
#         while cur_digit > 1:
#             # binary search (sorted list)
#             for i, digit in enumerate(digits):
#                 smallest_number: str = ''.join([digit] + [digits[0]]*(cur_digit-1))
#                 if smallest_number > n:
#                     break
#                 else:
#                     count += less_digits_count
#             cur_digit += 1

        
#         # Return
#         # number of positive integers
#         return total_count
        

        
# digits = [1, 2, 3],  n = 2100

# 2111

# 311
# 111

# 211
# 111

