class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # you should start from the edges because any element that is 
        # a part of pacific or atlantic needs to reach the border cells
        # if you perform dfs starting form the border cells, all cells that
        # become included in the dfs are valid cells for that specific ocean
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, prev, visit):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] < prev:
                return
            visit.add((r,c))
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
            return 

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)


        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res

