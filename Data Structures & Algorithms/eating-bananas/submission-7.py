class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float("inf")
        
        while l <= r:
            m = (l + r) // 2
            currTime = 0

            for p in piles:
                currTime += math.ceil(p/m)

            if currTime <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1


        return res
