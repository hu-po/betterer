# https://www.youtube.com/watch?v=4tYoVx0QoN0

from typing import List, Tuple
import queue

def remove_islands(board: List[List[int]]) -> List[List[int]]:
  """ Remove islands with basic python.  """
  
  # Space O(W + H + W*H) ~ O(W*H)
  # Time O(W + H + W*H + W*H) ~ O(W*H)

  w: int = len(board[0])
  h: int = len(board)

  mainland : Dict[Tuple[int, int], False] = {}
  to_explore = queue.Queue()

  for hi in (0, h-1):
    for wi in range(w):
      if board[hi][wi]:
        to_explore.put((hi, wi))
        mainland[(hi, wi)] = True
      
  for wi in (0, w-1):
    for hi in range(1, h-1):
      if board[hi][wi]:
        to_explore.put((hi, wi))
        mainland[(hi, wi)] = True

  def get_neighbors(i: int, j: int) -> Tuple[int, int]:
    for a in (-1, 1):
      if 0 <= i+a < h:
        yield i+a, j
      # else:
        # print(f'{i+a, j} is outside board')
      if 0 <= j+a < w:
        yield i, j+a
      # else:
        # print(f'{i, j+a} is outside board')

  # print(f'size {to_explore.qsize()}')
  # print(mainland)

  while not to_explore.empty():
    # print(to_explore.qsize())
    # print(mainland)
    hi, wi = to_explore.get()
    for hii, wii in get_neighbors(hi, wi):
      # print(f'checking {hii, wii}')
      if board[hii][wii]:
        if mainland.get((hii, wii), None) is None:
          # print(f'\n\n new addition at {hii, wii}')
          to_explore.put((hii, wii))
        mainland[(hii, wii)] = True
        
  board = [[0] * w for _ in range(h)]
  for hi, wi in mainland.keys():
    board[hi][wi] = 1

  return board

test = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1] 
]
sol = [
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1] 
]

# Check
np.array(sol) - np.array(remove_islands(test))
