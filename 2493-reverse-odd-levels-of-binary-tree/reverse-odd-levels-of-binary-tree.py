class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2, level):
            if not node1 or not node2:
                return
            
            # If the level is odd, swap the values
            if level % 2 == 1:
                node1.val, node2.val = node2.val, node1.val
            
            # Recur for the next level (left and right children)
            dfs(node1.left, node2.right, level + 1)
            dfs(node1.right, node2.left, level + 1)
        
        if root:
            dfs(root.left, root.right, 1)
        
        return root