class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {")": "(", "}":"{", "]":"["}

        for i in range(len(s)):
            if not stack and s[i] in bracket:
                return False
            else:
                if s[i] in bracket and bracket[s[i]] == stack[-1]:
                    stack.pop()
                elif s[i] in bracket:
                    return False
                else:
                    stack.append(s[i])

        if stack:
            return False
        else:
            return True