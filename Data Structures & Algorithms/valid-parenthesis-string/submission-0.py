class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1

                if leftMax < 0:
                    return False
                if leftMin < 0:
                    leftMin = 0
            else:
                leftMin -= 1
                leftMax += 1
                if leftMax < 0:
                    return False
                if leftMin < 0:
                    leftMin = 0

        if leftMin == 0:
            return True
        else:
            return False

