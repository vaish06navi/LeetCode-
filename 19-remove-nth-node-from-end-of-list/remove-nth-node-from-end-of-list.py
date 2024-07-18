# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        while temp is not None:
            temp = temp.next
            c += 1
        
        if c == n:
            head = head.next
            return head

        temp = head
        for i in range(c-n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head

class Solution:
    def removeNthFromEnd(self,head,n):
        res = ListNode(0,head)
        dummy = res

        for _ in range(n):
            head = head.next
        while head:
            head = head.next
            dummy = dummy.next
        dummy.next = dummy.next.next
        return res.next