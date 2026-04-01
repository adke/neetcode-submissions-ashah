class Solution:
    def decodeString(self, s: str) -> str:
        currNum = ""
        currWord = ""
        stack = []

        for c in s:
            if c.isdigit():
                currNum += c
            elif c == "[":
                stack.append(int(currNum))
                stack.append(currWord)
                currNum = ""
                currWord = ""
            elif c == "]":
                prevWord = stack.pop()
                prevNum = stack.pop()
                currWord = prevWord + (prevNum * currWord)

            else:
                currWord += c

        return currWord
