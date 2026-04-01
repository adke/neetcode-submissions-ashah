class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # MATRIX DFS QUESTION
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        def dfs(r, c, visit, height):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or height > heights[r][c]:
                return
            
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

            return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(0, c, pacific, heights[r][c])
                dfs(ROWS - 1, c, atlantic, heights[r][c])


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, 0, pacific, heights[r][c])
                dfs(r, COLS - 1, atlantic, heights[r][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])


        return res

        

        