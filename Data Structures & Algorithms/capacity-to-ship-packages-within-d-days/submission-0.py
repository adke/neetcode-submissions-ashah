class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = float("inf")

        def canShip(cap):
            # O(n) operation
            currCap = 0
            shipCount = 1
            for w in weights:
                currCap += w
                if currCap > cap:
                    shipCount += 1
                    currCap = 0
                    currCap += w
            return shipCount <= days

        while l <= r:
            midCap = (l + r) // 2
            if canShip(midCap):
                res = min(res, midCap)
                r = midCap - 1
            else:
                l = midCap + 1
        return res

