class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            shipCount = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    shipCount += 1
                    currCap = cap
                    currCap -= w
                else:
                    currCap -= w
            if shipCount <= days:
                return True
            else:
                return False
        
        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res