class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        count = 0
        for interval in intervals:
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[count:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                # need to merge the intervals
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            count += 1

        res.append(newInterval)
        return res