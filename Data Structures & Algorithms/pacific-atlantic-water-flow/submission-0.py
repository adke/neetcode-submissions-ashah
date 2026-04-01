class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        
        
        
        rows = len(heights)
        columns = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r,c,visited, prevHeight):
            if (r,c) in visited or r < 0 or c < 0 or r >= rows or c >= columns or heights[r][c] < prevHeight:
                return

            visited.add((r,c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])


        for i in range(columns):
            dfs(0, i, pacific, heights[0][i])
            dfs(rows - 1, i, atlantic, heights[rows - 1][i])

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, columns - 1, atlantic, heights[i][columns - 1])

        res = []

        for i in range(rows):
            for j in range(columns):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])

        return res


        