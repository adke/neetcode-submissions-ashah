class Solution:
    def isPalindrome(self, s: str) -> bool:
        processedString = ""

        for c in s:
            if c.isalnum():
                processedString += c.lower()
            else:
                continue

        l = 0
        r = len(processedString) - 1

        while l < r:
            if processedString[l] == processedString [r]:
                l += 1
                r -= 1
            else:
                return False

        return True