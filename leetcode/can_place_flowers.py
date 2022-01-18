class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # flowerbed with some plots planted (0 no flower, 1 flower)
        
        # flowers cannot be in adjacent plots
        
        # can we plant n flowers?
        
        # Are the plots already following the rule?
        
        # return (n <= (len(flowerbed)- sum(flowerbed)) // 2)
        
        # Time O(N * (1 + 1 + 1 + 1) + N * (1 + 1)) ~ O(N)
        # Space O(1) ~ O(1)
        
#         for i, planted in enumerate(flowerbed):
#             if planted == 1:
#                 if i-1 >= 0 and flowerbed[i-1] == 0:
#                     flowerbed[i-1] = -1
#                 if i+1 < len(flowerbed) and flowerbed[i+1] == 0:
#                     flowerbed[i+1] = -1
        
#         plots: int = 0
#         for available in flowerbed:
#             if available == 0:
#                 plots += 1
        
#         return n <= plots

#         plants: Iterable[int] = (i for i, planted in enumerate(flowerbed) if planted == 1)
#         next_plant: int = next(plants, None)
        
#         for i, planted in enumerate(flowerbed):
#             if next_plant is not None and i >= next_plant:
#                 next_plant = next(plants, None)
#             if planted == 1 and i+1 < len(flowerbed):                
#                 flowerbed[i+1] = 2
#             elif planted == 2:
#                 continue
#             elif next_plant is not None and i+1 == next_plant:
#                 flowerbed[i] == 2
#                 next_plant = next(plants, None)
#             else:
#                 # plant a flower
#                 n -= 1
#                 if n == 0:
#                     return True
#                 if i-1 >= 0 and flowerbed[i-1] == 0:
#                     flowerbed[i-1] = 2
#                 if i+1 < len(flowerbed) and flowerbed[i+1] == 0:
#                     flowerbed[i+1] = 2

#         return False
        
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                check_left: bool = (i-1 >= 0 and flowerbed[i-1] == 0) or (i-1 < 0)
                check_right: bool = (i+1 < len(flowerbed) and flowerbed[i+1] == 0) or (i+1 >= len(flowerbed))
                if check_left and check_right:
                    n -= 1
                    if n == 0:
                        return True
                    flowerbed[i] = 1
        return False
                    
                
            
