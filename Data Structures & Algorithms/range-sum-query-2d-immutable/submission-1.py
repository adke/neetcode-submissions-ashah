class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.prefixMap = [[0] * (self.COLS + 1) for i in range(self.ROWS + 1)]
        # prefix mapping logic (pre processing setup) - n^2 operation
        for r in range(self.ROWS):
            prefix = 0
            for c in range(self.COLS):
                prefix += matrix[r][c]
                above = self.prefixMap[r][c + 1]
                self.prefixMap[r + 1][c + 1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1
        total = self.prefixMap[r2][c2]
        topright = self.prefixMap[r1 - 1][c2]
        bottomleft = self.prefixMap[r2][c1 - 1]
        overlap = self.prefixMap[r1 - 1][c1 - 1]

        return total - topright - bottomleft + overlap


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)