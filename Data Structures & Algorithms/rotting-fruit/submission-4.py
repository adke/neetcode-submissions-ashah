class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # MATRIX BFS PROBLEM
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        q = deque()
        visit = set()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        def check(r, c, visit):
            # base case
            nonlocal fresh
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] != 1:
                return
            
            q.append([r,c])
            visit.add((r,c))
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))

        while q:
            qSize = len(q)
            for i in range(qSize):
                r,c = q.popleft()
                grid[r][c] = 2
                check(r + 1, c, visit)
                check(r - 1, c, visit)
                check(r, c + 1, visit)
                check(r, c - 1, visit)
            res += 1

        if fresh == 0:
            return res - 1
        else:
            return -1


