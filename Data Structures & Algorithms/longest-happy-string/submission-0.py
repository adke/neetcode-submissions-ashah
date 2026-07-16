class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = {}
        count["a"] = a
        count["b"] = b
        count["c"] = c

        heapp = []
        for c, v in count.items():
            if v != 0:
                heapp.append([-v, c])

        heapq.heapify(heapp)
        res = ""
        while heapp:
            c, char = heapq.heappop(heapp)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heapp:
                    break
                else:
                    c2, char2 = heapq.heappop(heapp)
                    res += char2
                    c2 += 1
                    if c2 != 0:
                        heapq.heappush(heapp, [c2, char2])
                    heapq.heappush(heapp, [c, char])
            else:
                res += char
                c += 1
                if c != 0:
                    heapq.heappush(heapp, [c, char])

        return res

