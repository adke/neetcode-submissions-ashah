class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        # check each row
        for i in range(rows):
            numSet = set()
            for j in range(cols):
                if board[i][j] in numSet:
                    return False
                elif board[i][j] != ".":
                    numSet.add(board[i][j])

        # check each column
        for i in range(cols):
            numSet = set()
            for j in range(rows):
                if board[j][i] in numSet:
                    return False
                elif board[j][i] != ".":
                    numSet.add(board[j][i])
        
        boards = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]

        for row, col in boards:
            numSet = set()

            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] in numSet:
                        return False
                    elif board[i][j] != ".":
                        numSet.add(board[i][j])

        return True