# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root, level):
            if not root: return 
            nonlocal res
            if len(res) < level + 1:
                res.append(root.val)
            traverse(root.right, level+1)
            traverse(root.left, level+1)
        
        traverse(root, 0)
        return res

