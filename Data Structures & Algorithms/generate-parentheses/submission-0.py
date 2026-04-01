class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def backTrack(OpenN, ClosedN):
            if OpenN == ClosedN == n:
                res.append("".join(stack))
                return
            
            if OpenN < n:
                stack.append("(")
                backTrack(OpenN + 1, ClosedN)
                stack.pop()

            if ClosedN < OpenN:
                stack.append(")")
                backTrack(OpenN, ClosedN + 1)
                stack.pop()
            
        backTrack(0,0)

        return res
            
