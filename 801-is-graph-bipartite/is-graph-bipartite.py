class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # bfs
        n = len(graph)

        self.isBiPart, colors, visited = True, [False for _ in range(n)], set()

        
        for i in range(n):
            if i in visited:
                continue

            queue = deque()
            queue.append(i)
            visited.add(i)

            while queue and self.isBiPart:
                node = queue.popleft()
                
                for g in graph[node]:
                    if g not in visited:
                        colors[g] = not colors[node]
                        queue.append(g)
                        visited.add(g)
                    else:
                        if colors[g] == colors[node]:
                            self.isBiPart = False
                            break

        return self.isBiPart