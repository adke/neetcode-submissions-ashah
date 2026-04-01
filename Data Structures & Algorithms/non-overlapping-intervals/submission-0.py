class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        recentInterval = [intervals[0]]
        res = 0

        for start, end in intervals[1:]:
            if start < recentInterval[-1][1]:
                recentInterval[-1][1] = min(recentInterval[-1][1], end)
                res += 1
            else:
                recentInterval.append([start, end])

        return res