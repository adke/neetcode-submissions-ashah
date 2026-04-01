class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c, curSet):
            # always start with base case
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in curSet or grid[r][c] != "1":
                return

            curSet.add((r,c))
            
            dfs(r + 1, c, curSet)
            dfs(r - 1, c, curSet)
            dfs(r, c + 1, curSet)
            dfs(r, c - 1, curSet)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c, visited)
                    res += 1

        return res