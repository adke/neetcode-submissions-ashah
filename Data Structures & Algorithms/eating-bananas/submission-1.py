class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            currentK = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / currentK)
            
            if hours <= h:
                res = min(currentK, res)
                r = currentK - 1
            else:
                l = currentK + 1
        return res


