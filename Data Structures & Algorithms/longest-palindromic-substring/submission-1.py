class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""

        # define pointers inside for loop
        for i in range(len(s)):
             l = i
             r = i # this will check odd lengths only

             while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    currSize = r - l + 1
                    if currSize > resLen:
                        resLen = currSize
                        res = s[l:r + 1]
                    l -= 1
                    r += 1
                else:
                    break
        # define pointers inside for loop
        for i in range(len(s)):
             l = i
             r = i + 1 # this will check even lengths only

             while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    currSize = r - l + 1
                    if currSize > resLen:
                        resLen = currSize
                        res = s[l:r + 1]
                    l -= 1
                    r += 1
                else:
                    break
        return res

        
