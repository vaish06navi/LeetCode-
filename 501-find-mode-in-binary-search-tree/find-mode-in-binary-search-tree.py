# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        mp = defaultdict(int)
        def helper(root,mp):
            if not root:
                return

            helper(root.left,mp)
            mp[root.val] += 1
            helper(root.right,mp)
        helper(root,mp)
        ans = []
        currFreq = 0
        for node,freq in mp.items():
            if freq > currFreq:
                ans = [node]
                currFreq = freq
            elif freq == currFreq:
                ans.append(node)
        return ans