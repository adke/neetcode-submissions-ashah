class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            currLen = r - l
            currVolume = currLen * min(heights[l], heights[r])
            maxVolume = max(maxVolume, currVolume)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxVolume