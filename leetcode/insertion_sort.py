# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # [2, 4, 1, 3]

        # Insertion
        # check node values from end until find one that is less
        # while (node that is more): 
        # if (node to be inserted).val < (node that is more).val
        #   (node before node that is more).next = (node to be inserted)
        #   (node to be inserted).next = (node that is more)
        # else
        #   (node that is more) = (node that is more).next
        #   (node before node that is more) = (node that is more)


        if not head or not head.next:
            return head
        
        # Space O(1 + 1 + 1) ~ O(1)
        # Time O(N * N) ~ O(N*2)
        
        dum: ListNode = ListNode(None, head)
        cur: ListNode = head
        run: ListNode = None
        tmp: ListNode  = None
        foo: ListNode = None
        while cur.next:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                run = dum
                tmp = cur.next
                cur.next = cur.next.next
                while run.next.val <= tmp.val:
                    run = run.next
                # run.next, tmp.next = tmp, run.next
                foo = run.next
                run.next = tmp
                tmp.next = foo
        return dum.next
