# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Space O(1 + 1 + 1 + 3 + 2) ~ O(8) ~ O(1)
        # Time O(N/2 + N/2 + N/2) ~ O(3 * 0.5 * N) ~ O(N)
        
        # Edge cases
        # head is None, list is of length 1
        if not head or not head.next or not head.next.next:
            return head
        
        # Algo
        # two pointers starting on opposite ends of the list
        # opposite ends means going through list once.
        # in-place
        
        # return pointer to head
        _p: ListNode = ListNode(val=None, next=head)
            
        # Find middle of linked list
        slow: ListNode = head
        fast: ListNode = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Cut lists appart
        middle: ListNode = slow.next
        slow.next = None
            
        # Reverse second half of linked list
        cur: ListNode = middle
        nxt: ListNode = None
        prv: ListNode = None
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        middle = prv
        
        # Merge both lists
        cur1: ListNode = head
        cur2: ListNode = middle
        _tmp1: ListNode = None
        _tmp2: ListNode = None
        while cur2:
            _tmp1 = cur1.next
            _tmp2 = cur2.next
            
            cur1.next = cur2
            cur2.next = _tmp1
            
            cur1 = _tmp1
            cur2 = _tmp2

        # Return
        return _p.next
        
#         # loop through the linked list
#         cur: ListNode = head
#         run: ListNode = None
#         nxt: ListNode = None

#         idx: int = 0
#         while cur.next:
#             nxt = cur.next
#             # Every even travel to end of list and get last node
#             if idx % 2 == 0:
#                 run = cur
#                 while run.next.next:
#                     run = run.next
#                 run.next.next = cur.next
#                 cur.next = run.next
#                 run.next = None      
#             idx += 1
#             cur = nxt
        
        


# [1, 2, 3, 4] - [1, 4, 2, 3]
# cur = 1, run = 2, idx = 0, cur.next = 2,
