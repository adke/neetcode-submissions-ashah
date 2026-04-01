class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            rowSet = set()
            currRow = board[i]

            for s in currRow:
                if s in rowSet:
                    return False
                elif s == ".":
                    continue
                else:
                    rowSet.add(s)

        for j in range(cols):
            colSet = set()
            
            for k in range(9):
                if board[k][j] in colSet:
                    return False
                elif board[k][j] == ".":
                    continue
                else:
                    colSet.add(board[k][j])


        miniBoards = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]

        for grid in miniBoards:
            row = grid[0]
            col = grid[1]
            gridSet = set()

            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] in gridSet:
                        return False
                    elif board[i][j] == ".":
                        continue
                    else:
                        gridSet.add(board[i][j])

        return True

                