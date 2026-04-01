class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        larray = [0] * len(height)
        rarray = [0] * len(height)
        res = 0

        for i in range(len(height)):
            larray[i] = maxL
            maxL = max(maxL, height[i])

        for i in range(len(height) - 1, -1, -1):
            rarray[i] = maxR
            maxR = max(maxR, height[i])

        for i in range(len(height)):
            potential = min(larray[i], rarray[i])
            actual = potential - height[i]
            if actual < 0:
                continue
            res += actual

        return res
