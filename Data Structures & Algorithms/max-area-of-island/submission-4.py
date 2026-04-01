class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS MATRIX GRAPH PROBLEM
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        maxRes = 0

        def dfs(r, c, visit):
            # base case
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] != 1:
                return 0 

            visit.add((r,c))

            return 1 + dfs(r + 1, c, visit) + dfs(r - 1, c, visit) + dfs(r, c + 1, visit) + dfs(r, c - 1, visit)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    res = dfs(r, c, visit)
                    maxRes = max(maxRes, res)

        return maxRes