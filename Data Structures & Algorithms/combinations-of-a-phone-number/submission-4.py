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

        if not digits:
            return []
        
        res = []

        def dfs(i, curr):
            if i == len(digits):
                res.append("".join(curr.copy()))
                return

            for j in range(len(digitToChar[digits[i]])):
                curr.append(digitToChar[digits[i]][j])
                dfs(i + 1, curr)
                curr.pop()

        dfs(0, [])

        return res






