class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS = n
        COLS = n
        res = []
        col = set()
        posDiag = set()
        negDiag = set()
        # create board first
        board = [["."] * n for i in range(ROWS)]

        def dfs(r):
            if r == n:
                boardStr = []
                for row in board:
                    boardStr.append("".join(row))
                res.append(boardStr)
                return

            for c in range(COLS):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                dfs(r + 1)
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

            return

        dfs(0)

        return res

            


            
        

        
