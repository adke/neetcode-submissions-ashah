class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i, height in enumerate(heights):
            if not stack:
                stack.append([i, height])
                continue
            else:
                startIndex = i
                while stack and height < stack[-1][1]:
                    stackIndex, stackHeight = stack.pop()
                    maxArea = max(maxArea, (i-stackIndex) * stackHeight)
                    startIndex = stackIndex
                stack.append([startIndex, height])

        if not stack:
            return maxArea
        else:
            for index, height in stack:
                maxArea = max(maxArea, (((len(heights) - 1) - (index)) + 1) * height)
            
            return maxArea