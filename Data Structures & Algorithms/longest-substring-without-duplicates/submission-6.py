class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # need to use a hashSet for this problem
        # we will be doing a linear scan on s so time-complexity: O(n)
        
        window = set()
        res = 0
        l = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l += 1
            window.add(s[i])
            res = max(res, i - l + 1)

        return res 