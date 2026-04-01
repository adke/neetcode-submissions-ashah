class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # use Multi-Source BFS
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()

        # helper function to check the neighbour of current cell that is popped from queue
        def checkNeighbour(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == -1:
                return
            q.append([r,c])
            visited.add((r,c))
        
        # add the gates to the q and visited set first
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                checkNeighbour(r + 1, c)
                checkNeighbour(r - 1, c)
                checkNeighbour(r, c + 1)
                checkNeighbour(r, c - 1)

            distance += 1