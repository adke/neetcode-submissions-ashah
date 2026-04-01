class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxSub = 0
        dupliSet = set()

        for r in range(len(s)):
            while s[r] in dupliSet:
                dupliSet.remove(s[l])
                l += 1

            dupliSet.add(s[r])
            currSize = (r - l) + 1
            maxSub = max(maxSub, currSize)

        return maxSub

