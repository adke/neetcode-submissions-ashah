class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxHeight = 0

        while l < r:
            currArea = min(heights[l], heights[r]) * (r - l)
            maxHeight = max(maxHeight, currArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxHeight
