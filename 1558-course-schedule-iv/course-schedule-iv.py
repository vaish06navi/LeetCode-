from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create graph and in-degree count
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        # Initialize reachability sets
        reachable = [set() for _ in range(numCourses)]
        
        # Perform topological sort
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            current = queue.popleft()
            
            # For each neighbor of the current node
            for neighbor in graph[current]:
                # Add all reachables of the current node to the neighbor
                reachable[neighbor].update(reachable[current])
                # Also add the current node itself as a prerequisite
                reachable[neighbor].add(current)
                
                # Decrease the in-degree and add to the queue if it reaches 0
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Answer queries based on reachability sets
        return [u in reachable[v] for u, v in queries]
