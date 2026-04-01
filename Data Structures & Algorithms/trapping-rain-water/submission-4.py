class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        left = []
        right = [0] * len(height)

        for i in range(len(height)):
            left.append(maxL)
            maxL = max(maxL, height[i])

        
        for i in range(len(height) - 1, -1, -1):
            right[i] = maxR
            maxR = max(maxR, height[i])

        res = 0

        for i in range(len(height)):
            potential = min(left[i], right[i]) - height[i]
            if potential < 0:
                continue
            else:
                res += potential

        return res

        