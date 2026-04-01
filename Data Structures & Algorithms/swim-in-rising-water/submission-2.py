class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # modified djisktra's algorithm
        # no need for adj list here since we already have grid
        # can check neighbors in the algo itself
        N = len(grid)
        visit = set()
        visit.add((0,0))
        minHeap = [[grid[0][0], 0, 0]]
        heapq.heapify(minHeap)
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            # check for valid neighbors
            for dx, dy in directions:
                x = r + dx
                y = c + dy
                if x < 0 or x == N or y < 0 or y == N or (x,y) in visit:
                    continue
                else:
                    heapq.heappush(minHeap, [max(t, grid[x][y]), x, y])
                    visit.add((x,y))


