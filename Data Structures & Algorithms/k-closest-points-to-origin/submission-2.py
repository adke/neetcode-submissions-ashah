class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        curr = []

        for i in range(len(points)):
            pt = points[i]
            curr.append([pt[0] ** 2 + pt[1] ** 2, pt])

        heapq.heapify(curr)

        while k != 0 :
            currPoint = heapq.heappop(curr)
            res.append(currPoint[1])
            k -= 1

        return res
        