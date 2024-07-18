# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        a.sort()

        if not a:
            return
        
        root = ListNode(a[0])
        curr = root
        for val in a[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return root
        