def reverseString(self, s: List[str]) -> None:
  """
  Do not return anything, modify s in-place instead.
  """
  for i in range(len(s)//2):
      s[len(s)-1-i], s[i] = s[i], s[len(s)-1-i]

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
      return head
  tmp = self.swapPairs(head.next.next) if head.next.next else None
  head, head.next = head.next, head
  head.next.next = tmp
  return head

