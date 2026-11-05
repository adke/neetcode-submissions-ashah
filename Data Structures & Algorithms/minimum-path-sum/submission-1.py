class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        lastRow = grid[-1]

        for c in range(COLS - 2, -1, -1):
            lastRow[c] = lastRow[c] + lastRow[c + 1] # lastRow can only go right to reach the end
        
        for r in range(ROWS - 2, -1, -1):
            currRow = grid[r]
            for c in range(COLS - 1, -1, -1):
                if c == COLS - 1:
                    currRow[c] = currRow[c] + lastRow[c]
                else:
                    currRow[c] = min(currRow[c] + currRow[c + 1], currRow[c] + lastRow[c])
            lastRow = currRow

        return lastRow[0]