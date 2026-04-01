class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window, target = {}, {}
        res, resLen = [-1, -1], float("inf")
        l = 0

        for c in t:
            target[c] = target.get(c, 0) + 1

        have = 0
        need = len(target)

        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1
           
            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1
                
            while have == need:
                currRes = r - l + 1
                if currRes < resLen:
                    res = [l, r]
                    resLen = currRes

                window[s[l]] -= 1

                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1

        

        if resLen < float("inf"):
            return s[res[0]: res[1] + 1]
        else:
            return ""
                   
            

        