class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def recursion(i,r,c):

            if i == len(word):
                return True

            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != word[i] or (r,c) in visited:
                return False

            visited.add((r,c))

            res = recursion(i + 1,r + 1,c) or recursion(i + 1,r - 1,c) or recursion(i + 1,r, c - 1) or recursion(i + 1,r,c + 1)

            visited.remove((r,c))

            return res

        for i in range(rows):
            for j in range(cols):
                if recursion(0, i, j):
                    return True

        return False