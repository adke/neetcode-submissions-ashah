class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        for s in path + "/":
            if s == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                
                curr = ""
            else:
                curr += s
        
        res = "/" + "/".join(stack) if stack else "/"

        return res