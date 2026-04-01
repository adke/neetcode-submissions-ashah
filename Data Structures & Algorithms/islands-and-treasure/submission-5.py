class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS Graph Traversal Question
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque([])
        visit = set()

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

        
        count = 0
        while q:
            for i in range(len(q)):
                currR, currC = q.popleft()
                grid[currR][currC] = count
                checkNei(currR + 1, currC, visit)
                checkNei(currR - 1, currC, visit)
                checkNei(currR, currC + 1, visit)
                checkNei(currR, currC - 1, visit)
            count += 1
            








