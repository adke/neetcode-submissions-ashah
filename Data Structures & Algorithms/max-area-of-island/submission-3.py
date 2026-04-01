class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r, c, curSet):
            # base case 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in curSet or grid[r][c] != 1:
                return 0

            curSet.add((r,c))

            return 1 + dfs(r + 1, c, curSet) + dfs(r - 1, c, curSet) + dfs(r, c + 1, curSet) + dfs(r, c - 1, curSet)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    currArea = dfs(r, c, visited)
                    maxArea = max(maxArea, currArea)

        return maxArea