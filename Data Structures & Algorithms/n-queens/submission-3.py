class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS = n
        COLS = n
        # 3 SETS
        posDiag = set()
        negDiag = set()
        cols = set()

        board = [["."] * n for i in range(n)]
        res = []

        def dfs(r):
            # BASE CASE
            if r == n:
                strBoard = []
                for row in board:
                    strBoard.append("".join(row))
                res.append(strBoard)
                return

            for c in range(n):
                if (c in cols) or (r + c in posDiag) or (r - c in negDiag):
                    continue
                # current cell is valid
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                dfs(r + 1)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
            return 

        dfs(0)
        return res

