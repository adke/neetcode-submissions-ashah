class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        mapChar = {}
        l = 0

        for r in range(len(s)):
            mapChar[s[r]] = mapChar.get(s[r], 0) + 1

            while((r - l + 1) - max(mapChar.values()) > k):
                mapChar[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
        