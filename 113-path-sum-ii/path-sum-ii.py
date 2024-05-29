# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return root

        ans = []
        def dfs(node,root):
            if node.left:
                dfs(node.left,res+[node.left])
            if node.right:
                dfs(node.right,res+[node.right])
            else:
                if sum(res) == targetSum or not root.left or root.right:
                    ans.append(res)
        dfs(root,[root.val])
        return ans

        




#-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path_recur(self, node, target, cur_path, all_paths):
        if not node:
            return
        cur_path.append(node.val)
        if node.val == target and not node.left and not node.right:
            all_paths.append(list(cur_path))
        else:
            self.find_path_recur(node.left, target-node.val, cur_path, all_paths)
            self.find_path_recur(node.right, target-node.val, cur_path, all_paths)
        cur_path.pop(-1)


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []
        self.find_path_recur(root, targetSum, [], out)
        return out