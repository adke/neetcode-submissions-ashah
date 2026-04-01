class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        count = 0
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                # check for overlapping here
                if interval[0] < res[-1][1]:
                    res[-1][1] = min(res[-1][1], interval[1])
                    count += 1
                else:
                    res.append(interval)
        return count
