class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        # range [lower, upper] 
        # sorted unique nums List[int] 
        # x is missing if x in range [lower, upper] and x not in nums
        
        # return smallest sorted list of ranges that covers every missing number
        
        
        # check inputs and edge cases
        
        if not nums:
            if lower == upper:
                return [f'{lower}']
            else:
                return [f'{lower}->{upper}']
        
        """
        [0, 1, 3], lower=-2, upper=4
        sol=['-2->-1']
            i=0
            i=1
        sol=['-2->-1', ]
        
        """
        
        # time O(1 + 1 + 1 + N + 1) ~ O(N)
        # space O(N) ~ O(N) where N is proportional to length of nums
        
        # go through list of nums, creating solution as we go
        sol: List[str]  = []   
            
        # start at low range
        if lower == nums[0] - 1:
            sol.append(f'{lower}')
        elif lower < nums[0]:
            sol.append(f'{lower}->{nums[0]-1}')
        
        # bounds for in-between nums
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                continue
            else:
                if nums[i+1] - nums[i] == 2:
                    sol.append(f'{nums[i]+1}')
                else:
                    sol.append(f'{nums[i]+1}->{nums[i+1]-1}')

        # end at the high range
        if upper == nums[-1] + 1:
            sol.append(f'{upper}')
        elif upper > nums[-1]:
            sol.append(f'{nums[-1]+1}->{upper}')
        
        return sol
