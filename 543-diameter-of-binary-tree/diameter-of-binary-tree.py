
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter =0
        def dfs(node):
            if not node:
                return 0
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            self.max_diameter = max(self.max_diameter , left_length+right_length)

            return 1 + max(left_length , right_length)
        dfs(root)
        return self.max_diameter
