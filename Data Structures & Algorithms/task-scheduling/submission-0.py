class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]

        q = deque()

        time = 0

        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            if len(maxHeap) != 0:
                currVal = heapq.heappop(maxHeap)
                currVal += 1
           
                if currVal:
                    q.append([currVal, time + n])

            if q and q[0][1] == time:
                qVal, idleTime = q.popleft()
                heapq.heappush(maxHeap, qVal)

        return time