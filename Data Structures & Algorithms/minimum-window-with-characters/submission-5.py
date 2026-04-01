class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minSize = float("inf")
        target = {}
        window = {}
        resIndex = []

        for c in t:
            target[c] = target.get(c, 0) + 1

        need = len(target)
        have = 0
        l = 0
        for r in range(len(s)):
            if s[r] in target:
                window[s[r]] = window.get(s[r], 0) + 1

                if window[s[r]] == target[s[r]]:
                    have += 1

                while have == need:
                    currSize = r - l + 1
                    if currSize < minSize:
                        minSize = currSize
                        resIndex = [l, r]
                    if s[l] in target:
                        window[s[l]] -= 1
                        if window[s[l]] < target[s[l]]:
                            have -= 1
                    l += 1

        if minSize == float("inf"):
            return ""
        else:
            return s[resIndex[0]:resIndex[1] + 1]




