class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}
        for x, y, z in times:
            adj[x].append([y,z])

        visit = set()
        minHeap = [[0, k]]
        heapq.heapify(minHeap)
        res = -1

        while minHeap:
            currWeight, currNode = heapq.heappop(minHeap)
            if currNode in visit:
                continue
            else:
                res = currWeight
                visit.add(currNode)
                for nei in adj[currNode]:
                    if nei[0] in visit:
                        continue
                    else:
                        heapq.heappush(minHeap, [currWeight + nei[1], nei[0]])
        
        if len(visit) == n:
            return res
        else:
            return -1

