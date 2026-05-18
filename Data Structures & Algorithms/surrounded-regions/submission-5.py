class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(r, c, visit):
            if r < 0 or c < 0 or (r,c) in visit or r == ROWS or c == COLS or board[r][c] != "O":
                return
            visit.add((r,c))
            board[r][c] = "T"
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
            return

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1 and board[r][c] == "O":
                    dfs(r, c, visit)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        
