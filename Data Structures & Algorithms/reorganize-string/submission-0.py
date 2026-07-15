class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        # should process higher frequency characters first
        heapp = []
        count = Counter(s)
        for char, c in count.items():
            heapp.append([-c, char])
        heapq.heapify(heapp)
        q = deque()

        time = 0
        while heapp or q:
            time += 1
            if heapp:
                currCount, c = heapq.heappop(heapp)
                if res and res[-1] != c or not res:
                    res += c
                else:
                    return ""
                currCount += 1

                if currCount != 0:
                    q.append([time + 1, currCount, c])

            if q and time == q[0][0]:
                _, cCount, char = q.popleft()
                heapq.heappush(heapp, [cCount, char])

        return res



