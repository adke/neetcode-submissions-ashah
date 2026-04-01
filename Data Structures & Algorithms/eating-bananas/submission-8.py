class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            curr = 0
            for p in piles:
                curr += math.ceil(p / mid) # round up always

            if curr > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1

        return res