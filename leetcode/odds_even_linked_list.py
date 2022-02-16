# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        head: ListNode > singly linked
        group all odd nodes then all even nodes
        first node is odd, then even, etc
        value doesn't matter, its just index
        
        test cases
        
        []
        return None

        [1]
        return 1

        [1,2,3,4]
        curr=1
        po=1
            pe=2,o=3,1>3,e=4,2>4,3>2,po=None  == 1,3,2,4
        return [1,3,2,4]
        
        [1,2,3,4,5]
        curr=1
        po=1
            pe=2,o=3,1>3,e=4,2>4,3>2,po=5  == 1,3,2,4,5
            pe=None,
            
            
        return [1,3,5,2,4]
        
        """
        
        # check inputs and edge cases
        
        if not head:
            return None
        
        if not head.next:
            return head
        
        if not head.next.next:
            return head
        
        # Go through the actual list
        o: ListNode = head
        e: ListNode = head.next
        eh: ListNode = e
            
        while e and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
            
        o.next = eh
        
        # time O(N)
        # space O(1)
            

        # return original head
        return head
        
        
        
