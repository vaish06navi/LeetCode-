class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        graph = defaultdict(list)

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1]*n
        low = [-1]*n

        result = []
        time = 0

        def dfs(node,parent):
            nonlocal time
            disc[node] = low[node] = time
            time += 1

            for neigh in graph[node]:
                if neigh == parent:
                    continue

                if disc[neigh] == -1: # If the neighbor is unvisited
                    dfs(neigh,node)
                    low[node] = min(low[node] , low[neigh] )
                    
                    # check if the edge is a criticial connection
                    if low[neigh] > disc[node]:
                        result.append([node , neigh])
                else:
                    low[node] = min(low[node] , disc[neigh])
        
        for i in range(n):
            if disc[i] == -1:
                dfs(i,-1)
        return result

