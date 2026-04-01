class MedianFinder:

    def __init__(self):
        self.minQ = []
        self.maxQ = []
        heapq.heapify(self.minQ)
        heapq.heapify(self.maxQ)
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.minQ, num * -1)
        if self.minQ and self.maxQ and ((self.minQ[0] * -1) > self.maxQ[0]):
            val = heapq.heappop(self.minQ) * -1
            heapq.heappush(self.maxQ, val)

        if abs(len(self.minQ) - len(self.maxQ)) > 1:
            # check which q is bigger and remove the element from there and push it into the other q
            if len(self.minQ) > len(self.maxQ):
                val = heapq.heappop(self.minQ) * -1
                heapq.heappush(self.maxQ, val)
            else:
                val = heapq.heappop(self.maxQ)
                heapq.heappush(self.minQ, val * -1)

    def findMedian(self) -> float:
        if len(self.minQ) > len(self.maxQ):
            return (self.minQ[0] * -1)
        elif len(self.maxQ) > len(self.minQ):
            return (self.maxQ[0])
        else:
            return ((self.minQ[0] * -1) + (self.maxQ[0])) / 2
        