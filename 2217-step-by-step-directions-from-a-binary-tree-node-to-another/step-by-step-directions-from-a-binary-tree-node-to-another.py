
class Solution:
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        start_path_from_root = []
        dest_path_from_root = []

        def traverse(node, path):
            nonlocal start_path_from_root 
            nonlocal dest_path_from_root

            # Early exit if both paths are found
            if not node or (start_path_from_root and dest_path_from_root):
                return
            
            # Copy the path to prevent being overwritten while traversing 
            if node.val == startValue:
               start_path_from_root = path.copy()
            elif node.val == destValue:
                dest_path_from_root = path.copy()

            # Backtracking path recoding
            path.append("L")
            traverse(node.left, path)
            path.pop()
            path.append("R")
            traverse(node.right, path)
            path.pop()

        # Traverse the tree and find the path to both nodes
        traverse(root, [])

        # Find the common path, i is the index where path differs
        # This step is to throw away the redundant common path
        i = 0
        while i < len(start_path_from_root) and i < len(dest_path_from_root):
            if start_path_from_root[i] == dest_path_from_root[i]:
                i += 1
            else:
                break
        
        # start (traverse UP) -> root -> dest
        return "".join(['U'] * (len(start_path_from_root) - i) + dest_path_from_root[i:])