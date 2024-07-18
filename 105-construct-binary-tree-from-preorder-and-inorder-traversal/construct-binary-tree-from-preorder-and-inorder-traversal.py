# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        partition_index = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:partition_index+1], inorder[:partition_index])
        root.right = self.buildTree(preorder[partition_index+1:], inorder[partition_index+1:])
            
        return root        
        