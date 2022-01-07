    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Iterative
        #   Time O(N)
        #   Space O(1)
        
#         if not head or not head.next:
#             return head        
#         prev: ListNode = None
#         curr: ListNode = head
#         tmp: ListNode = None
#         while curr:
#             tmp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = tmp
#         head = prev
#         return head
    
        # Recursive
        #   Time O(N)
        #   Space O(N)
        
        # base case
        if not head or not head.next:
            return head
        
        tmp: ListNode = self.reverseList(head.next)
        
        # point list back at itself
        head.next.next = head
        head.next = None

        return tmp
  
  def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # Space O(H)
        # Time O(H)
        
        if not root:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
          
from functools import cache

class Solution:
    
    @cache
    def getCell(self, colIndex: int, rowIndex: int) -> int:
        if colIndex < 1 or colIndex > rowIndex - 1  or rowIndex <= 1:
            return 1
        return self.getCell(colIndex - 1, rowIndex - 1) + self.getCell(colIndex, rowIndex - 1)
        
    def getRow(self, rowIndex: int) -> List[int]:
        return [self.getCell(colIndex, rowIndex) for colIndex in range(0, rowIndex + 1)]
