class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            colSet = set()
            for c in range(COLS):
                if board[r][c] in colSet:
                    return False
                elif board[r][c] == ".":
                    continue
                else:
                    colSet.add(board[r][c])

        for c in range(ROWS):
            rowSet = set()
            for r in range(COLS):
                if board[r][c] in rowSet:
                    return False
                elif board[r][c] == ".":
                    continue
                else:
                    rowSet.add(board[r][c])

        boards = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        for row, col in boards:
            newSet = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] in newSet:
                        return False
                    elif board[i][j] == ".":
                        continue
                    else:
                        newSet.add(board[i][j])

        return True



        