class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            visited.add((r,c))
            q = deque([(r,c)])

            while q:
                curRow, curCol = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    if (curRow + dr) in range(rows) and (curCol + dc) in range(cols) and grid[curRow + dr][curCol + dc] == "1" and ((curRow + dr, curCol + dc) not in visited):
                        q.append((curRow + dr, curCol + dc))
                        visited.add((curRow + dr, curCol + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands