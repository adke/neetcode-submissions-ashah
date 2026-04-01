class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window with a hashmap
        l = 0
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (((r - l + 1) - max(count.values())) > k):
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res