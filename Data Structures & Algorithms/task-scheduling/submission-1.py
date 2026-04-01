class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        heap = []
        for c in freq.values():
            heap.append(-c)

        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                count, _ = q.popleft()
                heapq.heappush(heap, count)

        return time

            