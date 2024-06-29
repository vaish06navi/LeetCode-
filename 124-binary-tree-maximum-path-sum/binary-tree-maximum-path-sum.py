# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        def DFS(root):
            if root == None:
                return 0

            lmax = DFS(root.left)
            rmax = DFS(root.right)

            lmax = 0 if lmax < 0 else lmax
            rmax = 0 if rmax <0 else rmax

            ans[0] = max(ans[0] , root.val+lmax+rmax)
            return root.val + max(lmax,rmax)
        DFS(root)
        return ans[0]
        