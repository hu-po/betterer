def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    # Length of list is one or zero
    if len(nums) <= 1:
        return 
    
    # Space: O(N)
    # Time: O(N)
    no_zeros = [num for num in nums if not num == 0]
    nums[:] = no_zeros + [0] * (len(nums) - len(no_zeros))


def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return []
        
        # Space O(N + C) ~ O(N)
        # Time O(N + N) ~ O(N)
        
        # How many of each integer in nums1?
        nums1_lookup = {}
        for num1 in nums1:
            num1_available = nums1_lookup.get(num1, None)
            if num1_available is not None:
                nums1_lookup[num1] += 1
            else:
                nums1_lookup[num1] = 1
            
        # How many intersect?
        intersec = []
        for num2 in nums2:
            num1_available = nums1_lookup.get(num2, None)
            if num1_available is not None and num1_available > 0:
                intersec += [num2]
                nums1_lookup[num2] -= 1
                
        return intersec

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
    if len(numbers) < 2:
        raise ValueError
    
    # Space O(C)
    # Time O(N)
    
    idx1 = 0
    idx2 = len(numbers) - 1
    
    while idx2 > idx1:
        if target - numbers[idx2] > numbers[idx1]:
            idx1 += 1                
        elif target - numbers[idx2] < numbers[idx1]:
            idx2 -= 1    
        else:
            return [idx1 + 1, idx2 + 1]

def maxProfit(self, prices: List[int]) -> int:

    if len(prices) <= 1:
        return 0

    # Space O(C + N) ~ O(N)
    # Time O(N + N) ~ O(N)

    lo_price = prices[0]    
    profit = [0] * len(prices)
    for day, price in enumerate(prices):
        lo_price = min(price, lo_price)
        profit[day] = price - lo_price
    return max(profit)