def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
    # Space O(2 + ) ~ O(C)
    # Time O(N + 0.5N) ~ O(N)
    
    node: ListNode = head
    length: int = 1
    
    # Get the length of the linked list
    while node.next is not None:
        length += 1
        node = node.next
        
    # Get the middle node
    node = head
    for _ in range((length // 2)):
        node = node.next
        
    return node

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
    # Length 1 list
    if head.next is None:
        return head.next
    
    # Space O(1 + 1) ~ O(1)
    # Time O(N + N) ~ O(N)
    
    slow: ListNode = head # (n - 1) node
    fast: ListNode = head # last node
        
    # Fast pointer "n" forward from slow pointer
    for _ in range(n):
        fast = fast.next
    
    # Small lists
    if fast is None:
        return head.next
    
    # Go until fast node reaches the end
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
        
    # Remove nth node
    slow.next = slow.next.next
    
    return head

def isValidSudoku(self, board: List[List[str]]) -> bool:

    # Space O(N)
    # Time O(N)
    
    accepted_values: List[str] = [str(n) for n in range(1, 10)]
    d: Dict[Tuple[str, int, int, int], bool] = {}
        
    for i in range(9):
        for j in range(9):
            if board[i][j] in accepted_values:
                
                # Check "Boxes"
                if d.get(('b', i//3, j//3, board[i][j]), None) is not None:
                    # print(f"Number at {i},{j} already exists in box {i//3},{j//3}")
                    return False
                else:
                    d[('b', i//3, j//3, board[i][j])] = True
                
                # Check column
                if d.get(('c', 0, j, board[i][j]), None) is not None:
                    # print(f"Number at {i},{j} already exists in column {j}")
                    return False
                else:
                    d[('c', 0, j, board[i][j])] = True
                
                # Check rows
                if d.get(('r', i, 0, board[i][j]), None) is not None:
                    # print(f"Number at {i},{j} already exists in row {i}")
                    return False
                else:
                    d[('r', i, 0, board[i][j])] = True

    return True