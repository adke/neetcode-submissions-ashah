class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        furthest = 0
        q = deque([0])

        while q:
            currIndex = q.popleft()
            start = max(furthest + 1, currIndex + minJump)

            for i in range(start, min(currIndex + maxJump + 1, len(s))):
                if s[i] == "0":
                    q.append(i)
                    if i == len(s) - 1:
                        return True
            furthest = currIndex + maxJump

        return False