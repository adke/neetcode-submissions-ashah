class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        q = deque()
        cycle = 0

        for v in freq.values():
            heap.append(-v)

        heapq.heapify(heap)

        while heap or q:
            cycle += 1
            if heap:
                curr = heapq.heappop(heap)
                curr += 1
                if curr != 0:
                    q.append([curr, cycle + n])

            if q and q[0][1] == cycle:
                newCycle, _ = q.popleft()
                heapq.heappush(heap, newCycle)

        return cycle


                    


