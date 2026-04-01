class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if len(t) > len(s):
            return ""

        window, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)
        l = 0
        res = [-1, -1]
        resLen = float('infinity')
        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                currWindow = r - l + 1
                if currWindow < resLen:
                    res = [l, r]
                    resLen = currWindow

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]: res[1] + 1]