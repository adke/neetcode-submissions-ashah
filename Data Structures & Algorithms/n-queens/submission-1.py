class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []

        # create board
        board = [["."] * n for i in range(n)]

        # DFS FUNCTION
        def dfs(r):
            # base case
            if r == n:
                currRes = ["".join(row) for row in board]
                res.append(currRes)
                return
            
            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negDiag:
                    continue

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


            
