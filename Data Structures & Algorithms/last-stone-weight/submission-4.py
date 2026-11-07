class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        else:
            heap = []
            for s in stones:
                heap.append(-s)
            heapq.heapify(heap)

            while len(heap) > 1:
                s1 = heapq.heappop(heap) * -1
                s2 = heapq.heappop(heap) * -1

                if s1 < s2:
                    heapq.heappush(heap, -1 * (s2 - s1))
                elif s2 < s1:
                    heapq.heappush(heap, -1 * (s1 - s2))

            if heap:
                return -1 * heap[0]
            else:
                return 0
                


            

