class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursion will be used here, specifically backtracking
        # why - to get all possibilities
        res = []

        def dfs(curr, openC, closedC):
            # base case
            if openC == closedC == n:
                res.append(curr)
                return

            if openC < n:
                curr += "("
                dfs(curr, openC + 1, closedC)
                curr = curr[:-1]
            
            if closedC < openC:
                curr += ")"
                dfs(curr, openC, closedC + 1)
                curr = curr[:-1]

        dfs("", 0, 0)
        return res