# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -float("inf")
        stack = deque()

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if prev >= root.val:
                return False

            prev = root.val
            root = root.right
        return True