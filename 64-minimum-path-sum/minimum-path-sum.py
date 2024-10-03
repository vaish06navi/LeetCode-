class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
#-------------------------------------------------------------------------------
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = [[float('inf')]*(cols+1) for r in range(rows+1)]
        res[rows-1][cols] = 0

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                res[r][c] = grid[r][c] + min(res[r+1][c] , res[r][c+1])
        return res[0][0]