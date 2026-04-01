class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = set()
        atlantic = set()

        res = []

        def dfs(r, c, prevH, curSet):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in curSet or heights[r][c] < prevH:
                return

            curSet.add((r,c))

            dfs(r + 1, c, heights[r][c], curSet)
            dfs(r - 1, c, heights[r][c], curSet)
            dfs(r, c + 1, heights[r][c], curSet)
            dfs(r, c - 1, heights[r][c], curSet)
            

        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(rows - 1, c, heights[rows - 1][c], atlantic)

        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, cols - 1, heights[r][cols - 1], atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res

        