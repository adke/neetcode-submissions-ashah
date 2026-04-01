class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closeN, s):
            if openN == closeN == n:
                curr = "".join(s)
                res.append(curr)
                return

            if openN < n:
                s.append("(")
                dfs(openN + 1, closeN, s)
                s.pop()

            if closeN < n and openN > closeN:
                s.append(")")
                dfs(openN, closeN + 1, s)
                s.pop()

        dfs(0, 0, [])

        return res