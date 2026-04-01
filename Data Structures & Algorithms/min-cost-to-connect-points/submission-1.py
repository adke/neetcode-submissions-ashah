class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}

        # need to create adj list first
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # now we need to apply normal prim's algo - MST ALGORITHM
        visit = set()
        minHeap = [[0,0]] # doesn't matter what point you start from
        res = 0
        heapq.heapify(minHeap)

        while minHeap:
            currCost, currNode = heapq.heappop(minHeap)
            if currNode in visit:
                continue
            visit.add(currNode)
            res += currCost

            for neiCost, neiNode in adj[currNode]:
                if neiNode not in visit:
                    heapq.heappush(minHeap, [neiCost, neiNode])
        
        return res

        