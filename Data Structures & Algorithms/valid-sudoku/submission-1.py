class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            currRow = board[i]
            rowSet = set()
            for s in currRow:
                if s in rowSet:
                    return False
                elif s == ".":
                    continue
                else:
                    rowSet.add(s)

        for i in range(9):
            colSet = set()
            for j in range(9):
                if board[j][i] in colSet:
                    return False
                elif board[j][i] == ".":
                    continue
                else:
                    colSet.add(board[j][i])

        subBoards = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]

        for row, col in subBoards:
            boardSet = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] in boardSet:
                        return False
                    elif board[i][j] == ".":
                        continue
                    else:
                        boardSet.add(board[i][j])


        return True

            