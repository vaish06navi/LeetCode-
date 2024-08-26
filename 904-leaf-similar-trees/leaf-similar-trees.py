class Solution:
    def leafSimilar(self,root1,root2):
        def dfs(node,arr):
            if node is None:
                return

            if node.left is None and node.right is None:
                arr.append(node.val)

            else:

                dfs(node.left,arr)
                dfs(node.right,arr)

        arr1 = []
        arr2 = []
        dfs(root1,arr1)
        dfs(root2,arr2)
        return arr1 == arr2