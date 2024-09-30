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

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        adj = [[] for _ in range(V)]

        # reverse the direction
        for i in range(V):
            for j in graph[i]:
                adj[j].append(i)

        # calculate the indegree
        indegree = [0]*V

        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
            
        # store the node with indegree = 0, in the queue
        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        # using kahn's algorithms and store the element in the list
        # basically we are detecting the cycle in the directed graph
        ans = []
        while (q):
            ele = q.popleft()
            ans.append(ele)

            for i in adj[ele]:
                if indegree[i] != 0:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
        return sorted(ans)
