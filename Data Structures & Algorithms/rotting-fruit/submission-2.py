class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        fresh = 0
        q = deque()

        def checkNeighbour(r, c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] != 1:
                return
            q.append([r,c])
            visited.add((r,c))
            fresh -= 1
        # can the number of fresh oranges at the beginning
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))

        minutes = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                checkNeighbour(r + 1, c)
                checkNeighbour(r - 1, c)
                checkNeighbour(r, c + 1)
                checkNeighbour(r, c - 1)
            if q:
                minutes += 1
        print(fresh)
        
        if fresh == 0:
            return minutes
        else:
            return -1




        