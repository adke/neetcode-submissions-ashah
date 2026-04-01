"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start.sort()
        end.sort()

        top, bot = 0, 0
        count = 0
        res = 0
        while top < len(start):
            if start[top] < end[bot]:
                count += 1
                top += 1
            else:
                count -= 1
                bot += 1
            
            res = max(res, count)

        return res
            