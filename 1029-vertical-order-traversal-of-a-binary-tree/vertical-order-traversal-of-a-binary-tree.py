from collections import defaultdict
from typing import Optional, List
from queue import Queue



class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(lambda: defaultdict(list))
        queue = Queue()

        queue.put((root, 0, 0))

        while not queue.empty():
            node, x, y = queue.get()
            nodes[x][y].append(node.val)

            if node.left:
                queue.put((node.left, x-1, y+1))
            if node.right:
                queue.put((node.right, x+1, y+1))

        result = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))
            result.append(col)
        return result
