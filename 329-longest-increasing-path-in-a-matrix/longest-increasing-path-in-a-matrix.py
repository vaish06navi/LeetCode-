class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        cache = [[-1 for _ in range(cols)] for _ in range(rows)]  # Memoization table
        
        def dfs(r, c):
            if cache[r][c] != -1:
                return cache[r][c]  # Return cached result if already computed
            
            # Possible directions (right, down, left, up)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            max_path = 1  # The length of the path is at least 1 (the current cell)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(nr, nc))  # Recursively find the longest path
            
            cache[r][c] = max_path  # Store the result in cache
            return max_path
        
        # Compute the longest increasing path for each cell
        longest_path = 0
        for r in range(rows):
            for c in range(cols):
                longest_path = max(longest_path, dfs(r, c))  # Update the longest path found
        
        return longest_path

