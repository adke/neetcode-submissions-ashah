class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS = n
        COLS = n
        cSet = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == ROWS:
                curr = []
                for j in range(len(board)):
                    curr.append("".join(board[j]))
                res.append(curr)
                return

            for c in range(COLS):
                if c in cSet or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                cSet.add(c)
                posDiag.add(r + c) 
                negDiag.add(r - c)              
                board[r][c] = "Q"
                dfs(r + 1)
                board[r][c] = "."
                cSet.remove(c)
                posDiag.remove(r + c) 
                negDiag.remove(r - c)  
            return

        dfs(0)

        print(board)

        return res
        