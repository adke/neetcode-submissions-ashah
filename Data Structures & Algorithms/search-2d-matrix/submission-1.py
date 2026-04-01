class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:

            mid = (top + bot) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break

        if not (top <= bot):
                return False

        left, right = 0, COLS - 1

        while left <= right:

            midNum = (left + right) // 2

            if matrix[mid][midNum] == target:
                return True
            elif matrix[mid][midNum] < target:
                left = midNum + 1
            else:
                right = midNum - 1
        
        return False

