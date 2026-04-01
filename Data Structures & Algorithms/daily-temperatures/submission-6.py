class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack question
        # temperatures needs to be strictly increasing
        
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                ind, oldTemp = stack.pop()
                res[ind] = i - ind
            stack.append([i,temp])

        return res