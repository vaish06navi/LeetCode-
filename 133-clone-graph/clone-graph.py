from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # If Given Node is None
        if not node:
            return None

        # Puttung Given Node in Queue
        queue = deque( [ node ] )    

        # Map which Stores "Original_Node : Same_Copied_Node"
        orig_copy_nodes_map = {}    

        orig_copy_nodes_map[node] = Node(val = node.val)

        # Traversing the Queue
        while queue:
            cur_node = queue.popleft()  # Take Front Guy

            # Traverse the Neighbours of Current_Node
            for neighbour in cur_node.neighbors:
                # If Neighbour is Not in Map
                if neighbour not in orig_copy_nodes_map:
                    orig_copy_nodes_map[neighbour] = Node(val = neighbour.val)
                    queue.append(neighbour)
                
                # Linking
                orig_copy_nodes_map[cur_node].neighbors.append(orig_copy_nodes_map[neighbour])
        
        return orig_copy_nodes_map[node]

        # Printing the 1st Node & It's Neighbours
        # print(node.val)
        # print(type(node.neighbors))
        # for i in node.neighbors:
        #     print(i.val)

        
