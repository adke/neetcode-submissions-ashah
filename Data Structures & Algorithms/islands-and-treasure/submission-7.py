class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # MULTI SOURCE BFS

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        def checkNei(r, c, visit):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1:
                return
            visit.add((r,c))
            q.append([r,c])
            return


        res = 0
        while q:
            currLen = len(q)
            for i in range(currLen):
                curr = q.popleft()
                r, c = curr[0], curr[1]
                grid[r][c] = res
                checkNei(r + 1, c, visit)
                checkNei(r - 1, c, visit)
                checkNei(r, c + 1, visit)
                checkNei(r, c - 1, visit)
            res += 1




