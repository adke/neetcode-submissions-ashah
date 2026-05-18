class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

        if not visit and not fresh:
            return 0
        elif not visit and fresh:
            return -1
        
        def checkNei(r, c, visit):
            nonlocal fresh
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] != 1:
                return
            visit.add((r,c))
            q.append([r,c])
            fresh -= 1
            return

        res = 0
        while q:
            currLen = len(q)
            for i in range(currLen):
                curr = q.popleft()
                r,c = curr[0], curr[1]
                checkNei(r + 1, c, visit)
                checkNei(r - 1, c, visit)
                checkNei(r, c + 1, visit)
                checkNei(r, c - 1, visit)
            res += 1

        if fresh == 0:
            return res - 1
        else:
            return -1

        

        
        