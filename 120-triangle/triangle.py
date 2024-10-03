class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle)-2,-1,-1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]



        # def dfs(row,col):
        #     if row == len(triangle)-1:
        #         return triangle[row][col]

        #     left = dfs(row+1,col)
        #     right = dfs(row+1,col+1)

        #     return triangle[row][col] + min(left,right)
        # return dfs(0,0)