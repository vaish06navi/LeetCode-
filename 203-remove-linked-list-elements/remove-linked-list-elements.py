# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return

        dummy = ListNode(val = -1,next = head)

        def recurse(prev,curr):
            if not curr:
                return
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
            recurse(prev,curr)
        recurse(dummy,head)
        return dummy.next

        
        