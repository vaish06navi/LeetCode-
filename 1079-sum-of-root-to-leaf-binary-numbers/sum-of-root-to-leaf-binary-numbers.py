# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root,str(root.val))]

        while stack:
            node,binval = stack.pop()

            if node.left:
                stack.append((node.left,binval+str(node.left.val)))
            if node.right:
                stack.append((node.right,binval+str(node.right.val)))

            if not node.left and not node.right:
                total += int(binval,2)
        return total
        