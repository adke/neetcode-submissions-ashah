class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kmin = 1
        kmax = max(piles)
        res = kmax

        while kmin <= kmax:
            kmid = (kmin + kmax) // 2
            time = 0

            for p in piles:
                time += math.ceil((float(p) / kmid))

            if time <= h:
                res = min(res, kmid)
                kmax = kmid - 1
            else:
                kmin = kmid + 1

        return res