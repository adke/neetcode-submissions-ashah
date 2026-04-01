class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braceMap = {')':'(', '}':'{', ']':'['}



        for c in s:
            if c in braceMap:
                if stack and stack[-1] == braceMap[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True
