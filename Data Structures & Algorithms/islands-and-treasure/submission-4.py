class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS Question
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visit = set()

        # Pre-processing
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        def checkNei(r, c, visit):
            # base case
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1:
                return
            
            q.append([r,c])
            visit.add((r,c))
            return

        # algorithm will run until q is empty
        count = 0
        while q:
            currLen = len(q)
            for i in range(currLen):
                row, col = q.popleft()
                grid[row][col] = count
                checkNei(row + 1, col, visit)
                checkNei(row - 1, col, visit)
                checkNei(row, col + 1, visit)
                checkNei(row, col - 1, visit)
            count += 1

        