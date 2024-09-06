class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Check if placing 'k' at position (r, c) is valid
        def isValid(r, c, k):
            for i in range(9):
                # Check row and column
                if board[i][c] == k or board[r][i] == k:
                    return False
                
                # Check the 3x3 subgrid
                subgrid_row = 3 * (r // 3) + i // 3
                subgrid_col = 3 * (c // 3) + i % 3
                if board[subgrid_row][subgrid_col] == k:
                    return False
            return True    

        # Recursively fill the board
        def fill(r, c):
            # If we reach the end of the board, the solution is found
            if r == 9:
                return True
            
            # Move to the next row if we reach the end of the current row
            if c == 9:
                return fill(r + 1, 0)
            
            # If the current cell is empty, try filling it
            if board[r][c] == '.':
                for k in range(1, 10):
                    if isValid(r, c, str(k)):
                        board[r][c] = str(k)
                        
                        # Recur for the next cell
                        if fill(r, c + 1):
                            return True
                        
                        # Backtrack if placing 'k' doesn't lead to a solution
                        board[r][c] = '.'
                
                # Return False if no valid number can be placed
                return False
            
            # Move to the next cell if the current one is already filled
            return fill(r, c + 1)

        # Start solving from the top-left corner
        fill(0, 0)