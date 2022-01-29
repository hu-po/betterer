# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # print(f'---- new test case {head} {left} {right}')
        
        if left > right:
            return head
        
        if not head or not head.next:
            return head
        
        if left == right:
            return head
        
        """
        [1, 2, 3, 4, 5], l=2, r=4
        
        dpNone  c1 > 2 > 3    prev = none, curr = 1, dumm = None
        pNone  c1 > d2 > 3    dumm = curr.next
        pNone < c1   d2 > 3    curr.next = prev
        None < pc1   d2 > 3    prev = curr
        None < p1   cd2 > 3    curr = dumm
        
        manually checking functions!
        [1, 2, 3, 4, 5], l=2, r=5
        og_head=n1
        i=1, curr=n1
            head=n1, curr=n2, i=2
        tail=n2
        dumm=none, prev=none
            dumm=n3, n2>none, prev=n2, curr=n3, i=3
            dumm=n4, n3>n2, prev=n3, curr=n4, i=4
            dumm=n5, n4>n3, prev=n4, curr=n5, i=5
        n5>n4
        
        [1, 2, 3, 4, 5], l=2, r=4
        og_head=n1
        i=1, curr=n1
            head=n1, curr=n2, i=2
        tail=n2
        dumm=none, prev=none
            dumm=n3, n2>none, prev=n2, curr=n3, i=3
            dumm=n4, n3>n2, prev=n3, curr=n4, i=4
            dumm=n5, n4>n3, prev=n4, curr=n5, i=5

        
        [3, 5], l=1, r=2
        head=n3
        og_head=n3
        i=1, curr=n3
        tail=n3
        dumm=none, prev=none
            dumm=n5, n3>none, prev=n3, curr=n5, i=2
        n5>n3
        return n5
            
        """
        
        # time.O(N) ~ O(N)
        # space.O(4) ~ O(1)
        
        # reverse a subset of the linked list
        
        # keep track of original head
        og_head: ListNode = head
        
        # moving head pointer to left index
        i: int = 1
        curr: ListNode = head
        while i < left:
            head = curr
            curr = curr.next
            i += 1
        tail: ListNode = curr
            
        # reverse linked list
        dumm: ListNode = None
        prev: ListNode = None
        while curr.next:
            dumm = curr.next
            curr.next = prev
            prev = curr
            curr = dumm
            i += 1
            if i - 1 == right:
                dumm = None
                break
                
        # fix up the ends
        if dumm is None:
            if left > 1:
                head.next = prev
                tail.next = curr
                return og_head
            else:
                head.next = curr
                return prev
        else:
            if left > 1:
                curr.next = prev
                head.next = curr
                # tail.next = None
                return og_head
            else:
                curr.next = prev
                return curr

        """
        [1, 2, 3, 4, 5], l=1, r=5
        head=n1, og_head=n1
        i=1, curr=n1
        tail=n1
        dumm=none, prev=none
            dumm=n2, n1>none, prev=n1, curr=n2, i=3
            dumm=n3, n2>n1, prev=n2, curr=n3, i=3
            dumm=n4, n3>n2, prev=n3, curr=n4, i=4
            dumm=n5, n4>n3, prev=n4, curr=n5, i=5
        n1>none
        return n5
        
        [1, 2, 3, 4, 5], l=1, r=4
        head=n1, og_head=n1
        i=1, curr=n1
        tail=n1
        dumm=none, prev=none
            dumm=n2, n1>none, prev=n1, curr=n2, i=3
            dumm=n3, n2>n1, prev=n2, curr=n3, i=3
            dumm=n4, n3>n2, prev=n3, curr=n4, i=4
            dumm=n5, n4>n3, prev=n4, curr=n5, i=5, dumm=None
        n1>n5
        return n4
        
        [1, 2, 3, 4, 5], l=2, r=5
        og_head=n1
        i=1, curr=n1
            head=n1, curr=n2, i=2
        tail=n2
        dumm=none, prev=none
            dumm=n3, n2>none, prev=n2, curr=n3, i=3
            dumm=n4, n3>n2, prev=n3, curr=n4, i=4
            dumm=n5, n4>n3, prev=n4, curr=n5, i=5
        n1>n5
        n2>none
        return n1
        
        [1, 2, 3, 4, 5], l=2, r=4
        og_head=n1
        i=1, curr=n1
            head=n1, curr=n2, i=2
        tail=n2
        dumm=none, prev=none
            dumm=n3, n2>none, prev=n2, curr=n3, i=3
            dumm=n4, n3>n2, prev=n3, curr=n4, i=4
            dumm=n5, n4>n3, prev=n4, curr=n5, i=5, dumm=None
        n1>n4
        n2>n5
        return n1
        """
                
        
        
        
        
        
            
        
        
        
