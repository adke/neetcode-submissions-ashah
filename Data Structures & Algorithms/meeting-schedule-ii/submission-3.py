"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        top = []
        bot = []

        for interval in intervals:
            top.append(interval.start)
            bot.append(interval.end)

        top.sort()
        bot.sort()

        t = 0
        b = 0
        count = 0
        res = 0

        while t < len(top):
            if top[t] < bot[b]:
                count += 1
                t += 1
            else:
                count -= 1
                b += 1
            
            res = max(res, count)

        return res
            
