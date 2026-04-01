class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                currIndex, currHeight = stack.pop()
                currArea = (i - currIndex) * currHeight
                res = max(currArea, res)
                startIndex = currIndex
            stack.append([startIndex, h])

        for i in range(len(stack)):
            curr = stack[i]
            currIndex, currHeight = curr[0], curr[1]
            res = max(res, ((len(heights)) - currIndex) * currHeight)

        return res


        