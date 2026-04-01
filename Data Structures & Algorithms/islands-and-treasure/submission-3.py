class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS Graph Problem
        # start with gate cells
        # GOLDEN RULE: WHEN ADDING CELLS TO Q, ADD IT TO VISIT SET AS WELL!
    
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
        count = 0
        # initialize q and visit set
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        def checkNei(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1:
                return
            q.append([r,c])
            visit.add((r,c))
            return

        while q:
            for i in range(len(q)):
                curRow, curCol = q.popleft()
                grid[curRow][curCol] = count
                checkNei(curRow + 1, curCol)
                checkNei(curRow, curCol + 1)
                checkNei(curRow - 1, curCol)
                checkNei(curRow, curCol - 1)
            count += 1

        