class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        stack = []
        for p, s in zip(position, speed):
            res.append([p, s])

        res.sort()

        for i in range(len(res) - 1, -1, -1):
            currPos, currSpeed = res[i][0], res[i][1]
            time = (target - currPos) / currSpeed
            stack.append(time)

            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
            
        return len(stack)


