class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""

        # odd cases only
        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                currSize = len(s[l:r + 1])
                if currSize > resLen:
                    resLen = currSize
                    res = s[l:r + 1]

                l -= 1
                r += 1

        # even cases
        for i in range(len(s)):
            l = i
            r = i + 1

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                currSize = len(s[l:r + 1])
                if currSize > resLen:
                    resLen = currSize
                    res = s[l:r + 1]

                l -= 1
                r += 1

        return res


        