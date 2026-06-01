class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openC, closeC, curr):
            if openC == closeC == n:
                res.append("".join(curr))
                return
            
            if openC < n:
                curr.append("(")
                dfs(openC + 1, closeC, curr)
                curr.pop()

            if closeC < openC:
                curr.append(")")
                dfs(openC, closeC + 1, curr)
                curr.pop()
            
            return

        dfs(0, 0, [])

        return res

            