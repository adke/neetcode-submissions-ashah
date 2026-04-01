class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        # 1 - 4 - example.1
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            currTime = 0
            for p in piles:
                currTime += math.ceil(p / mid)
            if currTime <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
            

