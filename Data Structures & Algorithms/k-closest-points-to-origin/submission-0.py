class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        count = 0
        for x,y in points:
            dist = (x ** 2) + (y ** 2)

            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        while count != k:
            currDist, currX, currY = heapq.heappop(minHeap)
            res.append([currX, currY])
            count += 1

        return res

