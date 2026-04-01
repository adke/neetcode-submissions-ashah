class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(r, c, visit):
            # base case
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 1
            elif (r,c) in visit:
                return 0
            else:
                visit.add((r,c))
                return dfs(r + 1, c, visit) + dfs(r - 1, c, visit) + dfs(r, c + 1, visit) + dfs(r, c - 1, visit)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c, visit)