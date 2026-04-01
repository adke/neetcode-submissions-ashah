class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c, curSet):
            # base case
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in curSet or grid[r][c] != 1:
                return 0

            curSet.add((r,c))
            
            return 1 + dfs(r + 1, c, curSet) + dfs(r - 1, c, curSet) + dfs(r, c + 1, curSet) + dfs(r, c - 1, curSet)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    # call dfs and return area
                    curArea = dfs(r, c, visited)
                    # compare this result with current maxArea and update accordingly
                    maxArea = max(curArea, maxArea)

        return maxArea

        