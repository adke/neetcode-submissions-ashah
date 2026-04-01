class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charCount = {}
        maxWindow = 0

        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)

            while ((r - l + 1) - max(charCount.values())) > k:
                charCount[s[l]] -= 1
                l += 1
            
            maxWindow = max(maxWindow, r - l + 1)
        return maxWindow


        