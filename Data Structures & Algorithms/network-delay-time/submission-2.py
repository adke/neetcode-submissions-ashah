class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        res = 0
        minHeap = [[0, k]]

        adj = {i:[] for i in range(1, n + 1)}
        for x,y,z in times:
            adj[x].append([y,z])

        heapq.heapify(minHeap)

        while minHeap:
            currRes, currNode = heapq.heappop(minHeap)
            if currNode in visit:
                continue
            else:
                res = max(currRes, res)
                visit.add(currNode)
                # now you check for neighbours
                for nei in adj[currNode]:
                    neiNode, weight = nei
                    if neiNode in visit:
                        continue
                    else:
                        heapq.heappush(minHeap, [weight + currRes, neiNode])
        
        return res if len(visit) == n else -1
