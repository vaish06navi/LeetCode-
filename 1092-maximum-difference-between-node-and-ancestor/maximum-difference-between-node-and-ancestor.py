# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        minv = root.val
        maxv = root.val
        return self.findMax(root, minv, maxv)

    def findMax(self, root, minv, maxv):
        if not root:
            return abs(minv - maxv)
        minv = min(minv, root.val)
        maxv = max(maxv, root.val)

        l = self.findMax(root.left, minv, maxv)
        r = self.findMax(root.right, minv, maxv)

        return max(l, r)