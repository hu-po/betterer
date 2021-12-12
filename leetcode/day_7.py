import queue
from typing import Dict

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        # Space O(C + C + C + N*M + N*M) ~ O(N*M)
        # Time O(C + N*M(C + 4*(C + C + C + C))) ~ O(N*M)
        
        h: int = len(image) 
        w: int = len(image[0])
        
        # Edge Cases
        # some of the rows are not the right length
        # image is empty
        # image is size 1 (vertically or horizontally)
        if not image or h < 1 or w < 1:
            return image
        
        # Algo
        # build a queue with neighbors to explore, keep track of nodes that we have already explored
        # modify the pixels in place
        # once exploration queue is empty, return image array

        to_explore: queue.Queue = queue.Queue()    
        to_explore.put((sr, sc))
        color: int = image[sr][sc]
        image[sr][sc] = newColor
        
        already_explored: Dict[Tuple[int, int], bool] = {(sr, sc) : True}
        
        def get_neighbors(row: int, col: int) -> Tuple[int, int]:
            # Up
            if row - 1 >= 0:
                yield row - 1, col
            # Down
            if row + 1 < h:
                yield row + 1, col
            # Left
            if col - 1 >= 0:
                yield row, col - 1
            # Right
            if col + 1 < w:
                yield row, col + 1
        
        while not to_explore.empty():
            row, col = to_explore.get()
            # print(f'Exploring {row},{col}')
            for row_n, col_n in get_neighbors(row, col):
                if already_explored.get((row_n, col_n), None) is not None:
                    continue
                else:
                    already_explored[(row_n, col_n)] = True
                    if image[row_n][col_n] == color:
                        image[row_n][col_n] = newColor
                        to_explore.put((row_n, col_n))

        # Return
        # image array with color replaced starting at image[sr][sc] using a flood fill
        # flood fill is 4 way connectivity
        return image

import queue
from typing import Set, List, Tuple

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # print('----------------')
        
        # Space O(1 + N*M + N*M + 1 + 1 + 1) ~ O(N*M)
        # Time O(1 + 1 + N*M*(4 + 1 + 1 + 1)) ~ O(N*M)
        
        h: int = len(grid)
        w: int = len(grid[0])
        
        # Edge Cases
        # grid is empty
        # rows in grid are different lengths
        # values in grid are not 0 or 1
        if not grid or h < 1 or w < 1:
            return 0
        
        if h == 1 and w == 1:
            return grid[0][0]
        
        # Algo
        # 4 point connectivity checker
        # search through the grid, which means exploration queue visited set
        # island property?
        # max island size?
        
        to_explore: queue.PriorityQueue = queue.PriorityQueue()
        
        # 0 is water
        # N is the island number
        visited: Set[Tuple[int, int]] = set()
    
        to_explore.put((grid[0][0] == 0, (0,0)))
        
        island_size: int = 0
        max_island_size: int = 0
        
        def get_neighbors(x: int, y: int) -> Tuple[int, int]:
            """ Return 4-way connectivity neighbors. """
            # Up
            if x - 1 >= 0 and not (x-1, y) in visited:
                yield x - 1, y
            # Down
            if x + 1 < h and not (x+1, y) in visited:
                yield x + 1, y
            # Left
            if y - 1 >= 0 and not (x, y-1) in visited:
                yield x, y - 1
            # Right
            if y + 1 < w and not (x, y+1) in visited:
                yield x, y + 1

        while not to_explore.empty():
            priority, (x, y) = to_explore.get()
            if grid[x][y] == 0:
                island_size = 0
            else:
                island_size = max(island_size, 1)
            # print(f'exploring {x}{y}, island size is {island_size}')
            for xn, yn in get_neighbors(x, y):
                if grid[xn][yn] == 0:
                    to_explore.put((1, (xn, yn)))
                else:
                    to_explore.put((0, (xn, yn)))
                    if grid[x][y] == 1:
                        island_size += 1
                        visited.add((xn, yn))
                    else:
                        break
                # print(f'checking neighbor {xn}{yn}, island size is {island_size}, max island size is {max_island_size}')
            visited.add((x, y))
            max_island_size = max(island_size, max_island_size)
            # print(f'visited {visited}')    

        # Return
        # max island area (land is 1, water is 0)
        # no islands return 0
        return max_island_size

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Space O(1)
        # Time O(N)
        
        # Edge Cases
        # empty list, list with only one element
        if not head or not head.next:
            return head
        
        # Algo
        # in place, check for vals being equal
        prev: ListNode = head
        curr: ListNode = head 
        while curr.next:
            curr = curr.next
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
        curr.next = None
        # Return
        # sorted linked list without duplicates
        return head   
        