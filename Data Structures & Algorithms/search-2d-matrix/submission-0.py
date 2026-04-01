class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            midRow = (top + bottom) // 2

            if matrix[midRow][-1] < target:
                top = midRow + 1
            elif matrix[midRow][0] > target:
                bottom = midRow - 1
            else:
                break
        
        if not (top <= bottom): #this means there is not a row in the matrix that contains the target
            return False

        l,r = 0, len(matrix[0]) - 1
        correctRow = (top + bottom) // 2

        while l <= r:
            midValue = (l + r) // 2

            if matrix[correctRow][midValue] > target:
                r = midValue - 1
            elif matrix[correctRow][midValue] < target:
                l = midValue + 1
            else:
                return True

        return False
        

           