# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # check inputs and edge cases
        if not list1 and not list2:
            return None
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        """
        l1=[], l2=[2,3]
            return [^2,3]
        l1=[], l2=[]
            return None
        l1=[^1,3], l2=[^2,3]
            head=[^1,3]
            curr=[^1,3]
            l1=[^3], l2=[^2,3]
                curr=[^1,2],l2=[^3],curr=[^2]
                curr=[^2,3],l2=None,curr=[^3]
                curr=[^3,3],l1=None,curr=[^3]
            return [^1,2,3,3]
        """
        
        # keep track of head node
        head: ListNode = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        # splice lists together in place
        curr: ListNode = head
        while list1 or list2:
            if list1 is None:
                curr.next = list2
                list2 = list2.next
            elif list2 is None:
                curr.next = list1
                list1 = list1.next
            elif list1.val >= list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        # time O(N) 
        # space O(N)
        # where N is the combined length of list1 and list2
            
        return head
