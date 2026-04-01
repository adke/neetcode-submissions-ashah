class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        stack = []
        # monotonic decreasing stack problem
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                currIndex, currTemp = stack.pop()
                arr[currIndex] = i - currIndex
            stack.append([i, t])
        
        return arr
