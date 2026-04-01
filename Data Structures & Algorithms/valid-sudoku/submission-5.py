class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            visitRow = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in visitRow:
                    return False
                else:
                    visitRow.add(board[r][c])

        for c in range(COLS):
            visitCol = set()
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in visitCol:
                    return False
                else:
                    visitCol.add(board[r][c])

        boards = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        for r,c in boards:
            visitBoard = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in visitBoard:
                        return False
                    else:
                        visitBoard.add(board[i][j])

        return True

        
