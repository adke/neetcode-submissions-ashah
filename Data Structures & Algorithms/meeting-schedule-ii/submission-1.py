"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : x.start)
        minHeap = []
        heapq.heapify(minHeap)

        for i in range(len(intervals)):
            if minHeap and minHeap[0] <= intervals[i].start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, intervals[i].end)

        return len(minHeap)