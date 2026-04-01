class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        l = 0
        r = x

        while l <= r:
            m = (l + r) // 2
            if m * m <= x:
                res = m
                l = m + 1
            else:
                r = m - 1

        return res