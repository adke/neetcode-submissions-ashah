class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        # use backtracking to get all possible combinations
        def backtrack(n, openN, closeN):
            # always consider base case to return from recursion
            if openN == closeN == n:
                curr = "".join(stack)
                res.append(curr)
                return

            if openN < n:
                stack.append("(")
                backtrack(n, openN + 1, closeN)
                stack.pop()


            if closeN < openN:
                stack.append(")")
                backtrack(n, openN, closeN + 1)
                stack.pop()

        backtrack(n, 0, 0)
                
        return res