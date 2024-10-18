class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ##############   Diagonal = row-col         AntiDiagonal = row+col       ##########

        def solver(row):
            if row == n:
                ans.append(["".join(i) for i in res])
                return
            for curr_col in range(n):
                curr_diag=row-curr_col
                curr_antiDiag=row+curr_col
                if curr_col not in col and curr_diag not in diag and curr_antiDiag not in antiDiag:
                    col.add(curr_col)
                    diag.add(curr_diag)
                    antiDiag.add(curr_antiDiag)
                    res[row][curr_col]="Q"

                    solver(row+1)

                    ####### Backtracking  ########

                    col.remove(curr_col)
                    diag.remove(curr_diag)
                    antiDiag.remove(curr_antiDiag)
                    res[row][curr_col]="."




        res=[["." for i in range(n)] for i in range(n)]
        col=set()
        diag=set()
        antiDiag=set()
        ans=[]
        solver(0)
        return ans