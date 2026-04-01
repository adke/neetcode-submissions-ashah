class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {")": "(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if not stack and c not in bracket:
                stack.append(c)
            elif c in bracket:
                if not stack:
                    return False
                elif bracket[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True
            