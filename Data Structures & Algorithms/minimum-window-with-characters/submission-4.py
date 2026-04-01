class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case
        if not t:
            return ""

        window = {}
        target = {}
        res = [0 , 0]
        resLen = float("inf")
        have = 0
        l = 0

        for c in t:
            target[c] = target.get(c , 0) + 1

        need = len(target)

        for r in range(len(s)):
            if s[r] in target:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == target[s[r]]:
                    have += 1
            
            while have == need:
                currLen = r - l + 1
                if currLen < resLen:
                    res = [l , r]
                    resLen = currLen
                if s[l] in target:
                    window[s[l]] -= 1
                    if window[s[l]] < target[s[l]]:
                        have -= 1
                l += 1

        if resLen != float("inf"):
            return s[res[0]: res[1] + 1]
        else:
            return ""
                