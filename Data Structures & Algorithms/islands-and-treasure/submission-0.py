class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()

        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        def addNeighbor(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r,c) in visited:
                return

            else:
                q.append([r,c])
                visited.add((r,c))
                return


        while q:

            for i in range(len(q)):
                r,c = q.popleft()

                grid[r][c] = distance

                addNeighbor(r + 1, c)
                addNeighbor(r - 1, c)
                addNeighbor(r, c + 1)
                addNeighbor(r, c - 1)

            distance += 1



                