class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxWindow = 0
        uniqueSet = set()

        for r in range(len(s)):
            while s[r] in uniqueSet:
                uniqueSet.remove(s[l])
                l += 1
            uniqueSet.add(s[r])
            maxWindow = max(maxWindow, (r - l) + 1)

        return maxWindow