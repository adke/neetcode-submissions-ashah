class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = set()
        atlantic = set()

        def dfs(r,c,curSet, prevHeight):
            # base case for a valid r,c
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in curSet or heights[r][c] < prevHeight:
                return
            
            curSet.add((r,c))

            dfs(r + 1, c, curSet, heights[r][c])
            dfs(r - 1, c, curSet, heights[r][c])
            dfs(r, c + 1, curSet, heights[r][c])
            dfs(r, c - 1, curSet, heights[r][c])

        for i in range(cols):
            dfs(0, i, pacific, heights[0][i])
            dfs(rows - 1, i, atlantic, heights[rows - 1][i])

        for j in range(rows):
            dfs(j, 0, pacific, heights[j][0])
            dfs(j, cols - 1, atlantic, heights[j][cols - 1])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res

        