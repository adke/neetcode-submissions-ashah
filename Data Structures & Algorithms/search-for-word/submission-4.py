class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use DFS to solve the problem
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c, visited, i):
            if i == len(word):
                return True
            elif r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r,c) in visited:
                return False

            visited.add((r,c))

            path1 = dfs(r + 1, c, visited, i + 1)
            path2 = dfs(r - 1, c, visited, i + 1) 
            path3 = dfs(r, c + 1, visited, i + 1)
            path4 = dfs(r, c - 1, visited, i + 1)

            visited.remove((r,c))

            return path1 or path2 or path3 or path4

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,visited,0):
                    return True

        return False
