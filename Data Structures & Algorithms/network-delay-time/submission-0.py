class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))
        t = 0
        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        visit = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for w2, n2 in adj[n1]:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        if len(visit) == n:
            return t
        else:
            return -1

