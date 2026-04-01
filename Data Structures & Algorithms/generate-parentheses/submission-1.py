class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(n, openC, closeC):
            # base case to return from backtrack

            if openC == closeC == n:
                curr = "".join(stack)
                res.append(curr)
                return

            if openC < n:
                stack.append("(")
                backtrack(n, openC + 1, closeC)
                stack.pop()
            
            if openC > closeC:
                stack.append(")")
                backtrack(n, openC, closeC + 1)
                stack.pop()

        backtrack(n, 0, 0)
        return res
