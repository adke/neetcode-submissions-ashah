class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            first = heapq.heappop(minHeap)
            second = heapq.heappop(minHeap)

            first = abs(first)
            second = abs(second)

            if second < first:
                heapq.heappush(minHeap, -(first - second))

        if len(minHeap) == 1:
            return -(minHeap[0])
        else:
            return 0