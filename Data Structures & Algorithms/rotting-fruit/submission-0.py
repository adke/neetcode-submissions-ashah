class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh > 0:

            for i in range(len(q)):

                r,c = q.popleft()

                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc

                    if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS or grid[newRow][newCol] != 1:
                        continue

                    grid[newRow][newCol] = 2
                    q.append([newRow, newCol])
                    fresh -= 1

            time += 1

        if fresh == 0:
            return time
        else:
            return - 1