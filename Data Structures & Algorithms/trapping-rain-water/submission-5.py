class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        
        curr = 0
        for i in range(len(height)):
            maxLeft[i] = curr
            curr = max(curr, height[i])

        curr = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = curr
            curr = max(curr, height[i])

        res = 0
        for i in range(len(height)):
            currWater = min(maxLeft[i], maxRight[i]) - height[i]
            if currWater <= 0:
                continue
            else:
                res += currWater

        return res
