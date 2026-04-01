class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.prefix = [[0] * (self.COLS + 1) for r in range(self.ROWS + 1)]
        # preWork needs to happen here
        for r in range(self.ROWS):
            rowSum = 0
            for c in range(self.COLS):
                r1, c1 = r + 1, c + 1
                rowSum += matrix[r][c]
                currPrefix = rowSum + self.prefix[r1 - 1][c1]
                self.prefix[r1][c1] = currPrefix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1 = row1 + 1, col1 + 1
        r2,c2 = row2 + 1, col2 + 1
        bottomRight = self.prefix[r2][c2]
        above = self.prefix[r1 - 1][c2]
        left = self.prefix[r2][c1 - 1]
        common = self.prefix[r1-1][c1-1]
        return bottomRight - above - left + common 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)