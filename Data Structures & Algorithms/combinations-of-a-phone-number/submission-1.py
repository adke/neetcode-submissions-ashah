class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

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

        def stringRecursion(i, currStr):
            if i == len(digits):
                res.append(currStr)
                return

            for c in digitToChar[digits[i]]:
                currStr = currStr + c
                stringRecursion(i + 1, currStr)
                currStr = currStr[:-1]

        
        if len(digits) != 0:
            stringRecursion(0, "")

        return res