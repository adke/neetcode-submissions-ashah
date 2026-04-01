class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # idea here is sort using the start time always, NEVER THE END TIME
        # then you only need to check if start time of current interval is strictly greater than end time of previous interval
             # -> if so, add the current interval to res and move to next interval
             # -> if not, you need to merge with previous interval (overwrite) then move to next interval
        # return res
        res = []
        intervals.sort() # sort by first element in inner-list by default
        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            else:
                # check to see if current interval will overlap with previous one
                if interval[0] <= res[-1][1]:
                    prevInterval = res.pop()
                    res.append([min(prevInterval[0], interval[0]), max(prevInterval[1], interval[1])])
                else:
                    res.append(interval)

        return res