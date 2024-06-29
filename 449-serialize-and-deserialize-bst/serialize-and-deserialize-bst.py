# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        
        def dfs(root):
            return [] if not root else [str(root.val)] + dfs(root.left) + dfs(root.right)
      
        return ' '.join(reversed(dfs(root)))
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
    
        def dfs(preorder, bound):
            if not preorder or int(preorder[-1]) > bound:
                return None
            node = TreeNode(int(preorder.pop()))
            node.left = dfs(preorder, node.val)
            node.right = dfs(preorder, bound)
            return node

        return dfs(data.split(), inf)
    



# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans