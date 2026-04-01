class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braceMap = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in braceMap and not stack:
                return False
            elif c in braceMap and stack[-1] == braceMap[c]:
                stack.pop()
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False