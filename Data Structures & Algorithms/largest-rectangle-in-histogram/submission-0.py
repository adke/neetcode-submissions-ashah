class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # stored with (startIndex, height)
        maxArea = 0

        for i, height in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > height:
                stackIndex, stackHeight = stack.pop()
                maxArea = max(maxArea, (i-stackIndex) * stackHeight)
                startIndex = stackIndex
            stack.append([startIndex, height])

        lastIndex = len(heights) - 1
        for i, height in stack:
            maxArea = max(maxArea, (lastIndex - i + 1) * height)

        return maxArea