class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairList = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p,s in sorted(pairList)[::-1]:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()

        return len(stack)