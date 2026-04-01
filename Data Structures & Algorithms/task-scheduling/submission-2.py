class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # need to use heap and deque
        freq = {}
        q = deque()
        minHeap = []
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        for c in freq.values():
            minHeap.append(-c)

        heapq.heapify(minHeap)

        time = 0
        while minHeap or q:
            time += 1

            if minHeap:
                cnt = heapq.heappop(minHeap)
                if cnt + 1 != 0:
                    q.append([cnt + 1, time + n])

            if q and q[0][1] == time:
                freqC, _ = q.popleft()
                heapq.heappush(minHeap, freqC)

        return time
        