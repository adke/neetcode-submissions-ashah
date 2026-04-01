class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        visit = set()
        cost = 0
        minHeap = [(0,0)]
        heapq.heapify(minHeap)

        while len(visit) < N:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            cost += w1

            for w2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2, n2))

        return cost



