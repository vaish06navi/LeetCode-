# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def IN(root,arr):
            if root is None:
                return
            else:
                IN(root.left,arr)
                arr.append(root.val)
                IN(root.right,arr)
            return arr
        return IN(root,[])
        