class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        visited = set()

        def dfs(start,end,path):

            # check if this path is valid or not
            if start == end:
                
                result.append(path + [start])
                return

            # add to path and visited
            visited.add(start)
            path.append(start)

            for node in graph[start]:
                if node not in visited:
                    dfs(node,end,path)

            path.pop()
            visited.remove(start)
        dfs(0,len(graph)-1 , [])

        return result

        