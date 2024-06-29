# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        res = TreeNode(0)
        curr = res
        
        def inorder(node):
            nonlocal curr  # Declare curr as nonlocal
            if not node:
                return

            inorder(node.left)
            node.left = None 
            curr.right = node
            
            # moving the pointer
            curr = curr.right 

            inorder(node.right)
    
        inorder(root)
        
        return res.right

        