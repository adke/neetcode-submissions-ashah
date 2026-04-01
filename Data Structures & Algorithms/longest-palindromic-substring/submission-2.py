class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSize = -1
        maxString = ""

        # first check all odd substrings
        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    currSize = r - l + 1
                    if currSize > maxSize:
                        maxSize = currSize
                        maxString = s[l:r + 1]
                    
                    l -= 1
                    r += 1
                else:
                    break

        # second check all even substrings
        for i in range(len(s)):
            l = i
            r = i + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    currSize = r - l + 1
                    if currSize > maxSize:
                        maxSize = currSize
                        maxString = s[l:r + 1]
                    
                    l -= 1
                    r += 1
                else:
                    break

        return maxString