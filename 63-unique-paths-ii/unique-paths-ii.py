class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dfs(obstacleGrid, 0, 0, memo)
    def dfs(self, obstacleGrid: List[List[int]], i: int, j: int, memo: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if i >= m or j >= n or obstacleGrid[i][j] == 1:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        if memo[i][j] != -1:
            return memo[i][j]
        memo[i][j] = self.dfs(obstacleGrid, i + 1, j, memo) + self.dfs(obstacleGrid, i, j + 1, memo)
        return memo[i][j]