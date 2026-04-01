class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            res.append([-((x ** 2) + (y ** 2)), x, y])

        heapq.heapify(res)

        while len(res) > k:
            heapq.heappop(res)

        newRes = []
        for dist, x, y in res:
            newRes.append([x,y])

        return newRes

        