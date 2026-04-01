class Solution:
    def isValid(self, s: str) -> bool:
        match = {"}": "{", "]" : "[", ")" : "("}
        stack = []

        for c in s:
            if c in match and not stack:
                return False
            elif c in match and stack[-1] != match[c]:
                return False
            elif c in match:
                stack.pop()
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False