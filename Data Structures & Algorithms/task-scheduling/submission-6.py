class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = []
        for c in count.values():
            q.append(-c)

        heapq.heapify(q)
        wait = deque()
        res = 0
        while q or wait:
            res += 1
            if q:
                curr = heapq.heappop(q)
                curr = curr + 1
                if curr != 0:
                    wait.append([res + n, curr])

            if wait and wait[0][0] == res:
                _ , task = wait.popleft()
                heapq.heappush(q, task)

        return res

