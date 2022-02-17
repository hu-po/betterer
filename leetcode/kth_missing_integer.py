class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        """
        arr: List[int] - sorted in increasing order
        k: int 
        find the kth integer missing from the array
        
        can k > len(arr) ?
        what happens if there aren't any missing integers?
        
        does arr start at 0 or 1?
        
        [1,3,5],k=2
        i=1
            num=1,i=2,
            num=3,k=1,i=3
            num=4
            
        
        """
        
        # time O(N)
        # space O(1 + 1) ~ O(1)
        
        # check inputs and edge cases
        if not arr:
            return None

        i: int = 1
        j: int = 0                    
        while k > 0 and j < len(arr):
            if not i == arr[j]:
                k -= 1
            else:
                j += 1
            i += 1
        if j < len(arr):
            return i - 1
        else:
            return arr[-1] + k
