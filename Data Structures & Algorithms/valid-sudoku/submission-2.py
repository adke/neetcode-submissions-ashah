class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            rowSet = set()
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rowSet:
                    return False
                else:
                    rowSet.add(board[i][j])

        for i in range(cols):
            colSet = set()
            for j in range(rows):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in colSet:
                    return False
                else:
                    colSet.add(board[j][i])

        subBoards = [[0,0], [0,3], [0,6], [3, 0], [3,3], [3,6], [6,0], [6,3], [6,6]]

        for r, c in subBoards:
            subSet = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in subSet:
                        return False
                    else:
                        subSet.add(board[i][j])

        return True

                

        
