class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        def fun(i,j):
            if i<0 or j<0 or i == rows or j == cols or not grid[i][j]:
                return 
            grid[i][j] = 0 # we can escape with this one so we make it 0
            fun(i+1,j)
            fun(i-1,j)
            fun(i,j+1)
            fun(i,j-1)
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j== 0 or j == cols-1) and grid[i][j]:
                    fun(i,j)        
        c = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    c += 1
        return c