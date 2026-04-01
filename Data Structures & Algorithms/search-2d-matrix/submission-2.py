class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
       
        l = 0
        r = len(matrix) - 1
        found = False
        while l <= r:
            m = (l + r) // 2

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                found = True
                break

        if not found:
            return False
        
        l = 0
        r = len(matrix[m]) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[m][mid] > target:
                r = mid - 1
            elif matrix[m][mid] < target:
                l = mid + 1
            else:
                return True

        return False
        

        