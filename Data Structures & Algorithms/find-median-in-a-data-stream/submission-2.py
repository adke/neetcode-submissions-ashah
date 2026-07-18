class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = [] # all elements in here must be >= all elements in small
        heapq.heapify(self.small)
        heapq.heapify(self.large)


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            curr = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, curr)

        # now we need to check if either heap is larger by 2
        if len(self.small) > len(self.large) + 1:
            curr = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, curr)
        elif len(self.large) > len(self.small) + 1:
            curr = heapq.heappop(self.large)
            heapq.heappush(self.small, curr * -1)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2
        
        