class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heapp = []

        for val in count.values():
            heapp.append(-val)

        heapq.heapify(heapp)

        res = 0
        q = deque()

        while heapp or q:
            res += 1
            if heapp:
                event = heapq.heappop(heapp)
                event += 1

                if event != 0:
                    q.append([event, res + n])

            if q and q[0][1] == res:
                event, _ = q.popleft()
                heapq.heappush(heapp, event)

        return res
