class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # length of the stack will give us the result
        res = []
        stack = []
        for pos, s in zip(position, speed):
            res.append([pos, s])

        res.sort()

        for i in range(len(res) - 1, -1, -1):
            curr = res[i]
            currTime = (target - curr[0]) / curr[1]
            stack.append(currTime)

            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
            
        return len(stack)