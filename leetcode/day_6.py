# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Space O(1 + 1) ~ O(1)
        # Time O(N + M) ~ O(N)
        
        # Edge Cases
        if list1 is None and list2 is None:
            return None
        
        # Pointers to merged list
        head: ListNode = ListNode()
        curr: ListNode = head

        # While either list still has a node left
        while (list1 is not None) or (list2 is not None):
            print(f'list 1 - {list1}')
            print(f'list 2 - {list2}')
            print('----')

            if list1 is None:
                curr.val = list2.val
                list2 = list2.next
                
            elif list2 is None:
                curr.val = list1.val
                list1 = list1.next
                
            elif (list2.val <= list1.val):
                curr.val = list2.val
                list2 = list2.next        
            
            elif (list1.val < list2.val):
                curr.val = list1.val
                list1 = list1.next
                
            # Make a new node
            if (list1 is not None) or (list2 is not None):
                curr.next = ListNode()
                curr = curr.next
            
        return head
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Space O(1 + 1 + 1) ~ O(1)
        # Time O(1 + N) ~ O(N)
        
        # Edge Cases
        # list is empty
        # list of length 1
        if not head or not head.next:
            return head
        
        # Algo
        # traverse through list
        # create new list in tandem (can this be done in place?)
        curr: ListNode = head
        prev: ListNode = None
        tmp: ListNode = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        return prev

class Solution:
    def isValid(self, s: str) -> bool:
        
        # Space O(1 + 1 + 1 + 1) ~ O(1)
        # Time O(1 + N) ~ O(N)
        
        # Edge Cases
        # string is empty or length 1
        if not s or len(s) <=1:
            return False
        
        # Algo
        # keep track of open/closed count for each type
        opened: List = []

        for char in s:
            if char == '(':
                opened.append(1)
            elif char == '{':
                opened.append(2)
            elif char == '[':
                opened.append(3)
            elif char == ')':
                if len(opened) == 0 or not opened.pop() == 1:
                    return False
            elif char == '}':
                if len(opened) == 0 or not opened.pop() == 2:
                    return False
            elif char == ']':
                if len(opened) == 0 or not opened.pop() == 3:
                    return False
                
        return len(opened) == 0

class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s = [x] + self.s

    def pop(self) -> int:
        if not self.empty():
            val = self.s[-1]
            self.s = self.s[:-1]
            return val
        return None

    def peek(self) -> int:
        if not self.empty():
            return self.s[-1]
        return None

    def empty(self) -> bool:
        if len(self.s) < 1:
            return True
        return False