class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(ROWS):
            if matrix[row][0] <= target and matrix[row][-1] >= target:
                top, bot = 0, COLS
                while top < bot:
                    mid = (top + bot) // 2
                    if target > matrix[row][mid]:
                        top = mid + 1
                    elif target < matrix[row][mid]:
                        bot = mid
                    else:
                        return True
        return False