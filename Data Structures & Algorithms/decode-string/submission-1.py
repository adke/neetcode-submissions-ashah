class Solution:
    def decodeString(self, s: str) -> str:
        currStr = ""
        currNum = ""
        stack = []

        for c in s:
            if c.isdigit():
                currNum += c
            elif c == "[":
                stack.append(currStr)
                stack.append(int(currNum))
                currStr = ""
                currNum = ""
            elif c == "]":
                stackNum = stack.pop()
                stackStr = stack.pop()
                currStr = stackStr + (stackNum * currStr)
            else:
                currStr += c
        
        return currStr