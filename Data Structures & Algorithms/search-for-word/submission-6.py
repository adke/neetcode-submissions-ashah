class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # need to call recursion on every cell
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(i, r, c, visit):
            if i == len(word):
                return True
            elif (r,c) in visit or r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != word[i]:
                return False
            else:
                visit.add((r,c))
                res = dfs(i + 1, r + 1, c, visit) or dfs(i + 1, r, c + 1, visit) or dfs(i + 1, r - 1, c, visit) or dfs(i + 1, r, c -1, visit)
                visit.remove((r,c))
                return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c, visit):
                    return True
        
        return False




                
