class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = nums
        heapq.heapify(res)
        count = len(res) - k # number of times we need to pop from minHeap
        
        while count:
            heapq.heappop(res)
            count -= 1

        return res[0]