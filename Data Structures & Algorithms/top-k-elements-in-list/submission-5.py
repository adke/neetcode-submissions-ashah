class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        c = Counter(nums)

        for n, count in c.items():
            res.append((-count, n))

        heapq.heapify(res)
        
        final = []
        while k != 0:
            _, number = heapq.heappop(res)
            final.append(number)
            k -= 1
        
        return final


