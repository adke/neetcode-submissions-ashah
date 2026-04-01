class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minHeap = []

        for n in nums:
            minHeap.append(-n)

        heapq.heapify(minHeap)
        counter = 0 

        while counter < k:
            res = heapq.heappop(minHeap)
            counter += 1

        return -res
        