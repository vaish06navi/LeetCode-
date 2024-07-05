# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLength(self,head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def reverseGroup(self,head,k,length):
        if length < k:
            return head

        curr = head
        prev = None
        next = None
        count = 0
        while curr and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        if next:
            head.next = self.reverseGroup(next,k,length-k)
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.getLength(head)
        return self.reverseGroup(head,k,length)
