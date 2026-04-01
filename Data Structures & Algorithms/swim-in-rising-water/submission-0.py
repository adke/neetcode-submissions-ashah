class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        directions = [[0,1], [0,-1], [1,0],[-1,0]]
        minHeap = [(grid[0][0], 0, 0)]
        visit.add((0,0))
        heapq.heapify(minHeap)

        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return height

            for dr, dc in directions:
                r1 = r + dr
                c1 = c + dc

                if r1 < 0 or r1 == N or c1 < 0 or c1 == N or (r1, c1) in visit:
                    continue
                visit.add((r1, c1))
                heapq.heappush(minHeap, (max(height, grid[r1][c1]), r1, c1))

        