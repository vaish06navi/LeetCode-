# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,currGreatest):
            nonlocal res
            if not root:
                return

            if root.val >= currGreatest:
                res += 1

            currGreatest = max(currGreatest,root.val)
            dfs(root.left,currGreatest)
            dfs(root.right,currGreatest)
        res = 0
        dfs(root,root.val)
        return res
        