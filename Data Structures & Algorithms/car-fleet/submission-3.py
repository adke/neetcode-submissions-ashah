class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        stack = []

        for p, s in zip(position, speed):
            arr.append([p,s])
        
        arr.sort()
        arr.reverse()

        for p,s in arr:
            time = ((target-p)/s)
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)