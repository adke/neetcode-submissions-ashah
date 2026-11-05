class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        lastRow = [1] * COLS

        for c in range(COLS - 1, -1, -1):
            if obstacleGrid[ROWS - 1][c] == 1:
                lastRow[c] = 0
            elif c == COLS -1:
                continue
            else:
                lastRow[c] = lastRow[c + 1]
        
        for r in range(ROWS - 2, -1, -1):
            currRow = [1] * COLS
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    currRow[c] = 0
                elif c == COLS - 1:
                    currRow[c] = lastRow[c]
                else:
                    currRow[c] = currRow[c + 1] + lastRow[c]
            lastRow = currRow

        return lastRow[0]
        
