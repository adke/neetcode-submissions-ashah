class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracesMap = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in bracesMap:
                if stack and stack[-1] == bracesMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        else:
            return False
        