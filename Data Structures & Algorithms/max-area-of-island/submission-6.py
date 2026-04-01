class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS Matrix Graph Traversal Pattern
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(r, c, visit):
            # BASE CASE ALWAYS FIRST
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] != 1:
                return 0
            
            visit.add((r,c))
            
            return 1 + dfs(r + 1, c , visit) + dfs(r - 1, c , visit) + dfs(r, c + 1, visit) + dfs(r, c - 1, visit)

        res = 0
        for r in range(ROWS): 
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    currArea = dfs(r, c, visit)
                    res = max(res, currArea)

        return res
