from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        # Initialize distances with infinity
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        
        # Start with all 0 cells in the queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        # Directions for moving up, down, left, and right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS to update distances
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If in bounds and we find a shorter path to (nx, ny)
                if 0 <= nx < rows and 0 <= ny < cols:
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
        
        return dist