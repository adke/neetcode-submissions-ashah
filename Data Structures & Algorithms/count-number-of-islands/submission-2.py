class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c, curSet):
            # base case always comes first
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in curSet or grid[r][c] != "1":
                return
            
            curSet.add((r,c))

            dfs(r + 1, c, curSet)
            dfs(r - 1, c, curSet)
            dfs(r, c + 1, curSet)
            dfs(r, c - 1, curSet)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # call dfs
                    dfs(r,c,visited)
                    # increment res by 1
                    res += 1

        return res

            