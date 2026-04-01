class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS Question
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(r, c, visit, i):
            # base case
            if i == len(word):
                return True
            elif r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] != word[i]:
                return False

            visit.add((r,c))

            res = dfs(r + 1, c, visit, i + 1) or dfs(r - 1, c, visit, i + 1) or dfs(r, c + 1, visit, i + 1) or dfs(r, c - 1, visit, i + 1)

            visit.remove((r,c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,visit,0):
                    return True

        return False

      