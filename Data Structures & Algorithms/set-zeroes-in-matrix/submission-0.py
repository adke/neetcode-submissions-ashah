class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        firstRowHeader = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:

                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                       firstRowHeader = True

        for r in range(1, rows):
            for c in range(1, cols): 
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0

        if firstRowHeader:
            for i in range(cols):
                matrix[0][i] = 0

    
