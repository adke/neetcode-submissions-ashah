class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        visit = set()
        maxWindow = 0

        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1

            visit.add(s[r])
            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow