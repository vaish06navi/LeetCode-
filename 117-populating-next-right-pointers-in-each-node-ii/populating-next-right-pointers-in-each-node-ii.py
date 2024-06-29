"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return None
  
                
        if root.left:
            if root.right:
              root.left.next=root.right 
            else:
             curr=root.next
             while curr!=None:
                if curr.left:
                    root.left.next=curr.left
                    break
                elif curr.right:
                    root.left.next=curr.right
                    break
                curr=curr.next
        if root.right:
            curr=root.next
            while curr!=None:
                if curr.left:
                    root.right.next=curr.left
                    break
                elif curr.right:
                    root.right.next=curr.right
                    break
                curr=curr.next
        self.connect(root.right) ##right side always first processed
        self.connect(root.left)
        

        return root
