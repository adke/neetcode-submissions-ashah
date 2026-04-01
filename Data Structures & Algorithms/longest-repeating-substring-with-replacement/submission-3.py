class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxWindow = 0
        hashM = {}

        for r in range(len(s)):
            hashM[s[r]] = hashM.get(s[r], 0) + 1

            while(((r - l + 1) - max(hashM.values())) > k):
                hashM[s[l]] -= 1
                l += 1

            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow