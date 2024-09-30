# Approach:
# - Reverse the graph: Track incoming edges instead of outgoing ones.
# - Use Topological Sorting with a queue to perform a reverse BFS starting from terminal nodes.
# - Nodes that reach terminal nodes in this reversed graph are marked as safe.

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
 
            visited[node] = True
            for neig in graph[node]:
                if dfs(neig):
                    return True
                
            visited[node] = False

        for i in range(len(graph)):
            if not dfs(i):
                res.append(i)
        return res
