def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    
    if len(s) <= 1:
        return
    
#         if not all([0 < len(_) < 2 for _ in s]):
#             raise ValueError('This is not what was promised')
    
    # # Built-in
    # s[:] = list(reversed(s))
    
    # # Slicing
    # s[:] = s[::-1]
    
    # Space O(1 + 1 + 1) ~ O(1)
    # Time O(0.5*N) ~ O(N) 
    
    # Dark Ages
    tmp = 0
    l = len(s)
    i = 0
    while i < l//2:
        tmp = s[i]
        s[i] = s[l-1-i]
        s[l-1-i] = tmp
        i += 1
            
# ['h', 'i']
# ['w', 'o', 'w']

def reverseWords(self, s: str) -> str:
        
    # Space O(0.2N) ~ O(N)
    # Time O(0.2N + N) ~ O(N)
    
    if len(s) <= 1:
        return s
    
    words = [list(word) for word in s.split(' ')]
    
    for word in words:
        word[:] = word[::-1]
        
    return ' '.join([''.join(word) for word in words])

def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
    # Space O(N + N + C) ~ O(N)
    # Time O(N + C + N) ~ O(N)
    
    if r <= 0 or c <= 0:
        return mat
    
    if not (r * c) == len(mat) * len(mat[0]):
        return mat
    
    if not all([len(row) == len(mat[0]) for row in mat]):
        return mat
    
    # Old School
    m_reshaped = [[0] * c for _ in range(r)]    
    i = 0
    j = 0
    for row in mat:
        for n in row:
            m_reshaped[i][j] = n
            if j < c - 1:
                j += 1
            else:
                j = 0
                i += 1
    return m_reshaped

    # # Numpy
    # return np.array(mat).reshape((r, c)).tolist()

def next_row(self, prev_row : List[int]) -> List[int]:
    """ Return the next row in the fibonacci triangle given previous row. """
    new_row = [1] * (len(prev_row) + 1)
    for i in range(1, len(prev_row)):
        new_row[i] = prev_row[i - 1] + prev_row[i]
    return new_row


def generate(self, numRows: int) -> List[List[int]]:
    
    # Space O(C + N * (N/2)) ~ O(N*N)
    # Time O(C + N) ~ O(N*N)
    
    pt = [[1], [1, 1], [1, 2, 1]]
    if numRows < 4:
        return pt[:numRows]
    
    for _ in range(numRows - 3):
        new_row = self.next_row(pt[-1])
        pt += [new_row]
        
    return pt