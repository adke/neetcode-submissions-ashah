class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window problem with hashset
        # substring is different than subsequence
        # substring -> needs to be contiguous
        # subsequence -> doesn't have to be
        l = 0
        visit = set()
        res = 0

        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])

            currLen = r - l + 1
            res = max(currLen, res)

        return res