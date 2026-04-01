class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(r, c, visit):
            # base case
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] != "1":
                return

            visit.add((r,c))

            dfs(r + 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r - 1, c, visit)
            dfs(r, c - 1, visit)

            return
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r, c, visit)
                    res += 1

        return res
