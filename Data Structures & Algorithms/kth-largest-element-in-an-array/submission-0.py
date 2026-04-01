class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        counter = 0

        heapq.heapify(maxHeap)

        while True:
            currVal = heapq.heappop(maxHeap)
            counter += 1

            if counter == k:
                return - currVal



