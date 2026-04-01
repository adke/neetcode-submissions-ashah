class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x : x[0])
        minHeap = []
        heapq.heapify(minHeap)
        res = {}
        final = []
        i = 0

        # first check and add the intervals that the query belongs to into the heap
        for q in sorted(queries): # don't change the actual order of queries
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1

        for q in queries:
            final.append(res[q])

        return final

                
        # then pop any intervals in the heap that don't belong to the query
        
        # it is guranteed that the intervals you pop don't belong to any
        # other queries that will come after


