"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        
        # edge case
        if not intervals or len(intervals) == 1:
            return True
        
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True