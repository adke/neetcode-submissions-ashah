class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS Problem
        # initialize variables
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()
        count = 0

        # initialize queue with first values
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        # create helper function to check neighbors
        def checkNei(r, c, visit):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == -1:
                return
            q.append([r,c])
            visit.add((r,c))

        # implement core BFS logic
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = count
                # check neighbor
                checkNei(r + 1, c, visited)
                checkNei(r - 1, c, visited)
                checkNei(r, c + 1, visited)
                checkNei(r, c - 1, visited)
            count += 1

        
        