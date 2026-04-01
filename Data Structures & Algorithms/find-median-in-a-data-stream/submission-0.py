class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # ensure all numbers in small heap are smaller than large heap
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # ensure the len between two heaps at most differ by 1
        if abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                val = heapq.heappop(self.small) * -1
                heapq.heappush(self.large, val)
            else:
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2
        