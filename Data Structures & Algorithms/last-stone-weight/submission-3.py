class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
            
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            s1 *= -1
            s2 *= -1

            if s1 < s2:
                heapq.heappush(stones, (s2 - s1) * -1)
            elif s2 < s1:
                heapq.heappush(stones, (s1 - s2) * -1)
            else:
                continue

        if stones:
            return stones[0] * -1
        else:
            return 0




