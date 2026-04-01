class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # RECURSION, WANT ALL POSSIBLITIES FOR DIGITS (RECURSION)
        currStr = []
        res = []
        def dfs(i):
            # base case
            if len(currStr) == len(digits):
                res.append("".join(currStr))
                return

            for c in digitToChar[digits[i]]:
                currStr.append(c)
                dfs(i + 1)
                currStr.pop()

        if digits:
            dfs(0)
            return res
        else:
            return []

