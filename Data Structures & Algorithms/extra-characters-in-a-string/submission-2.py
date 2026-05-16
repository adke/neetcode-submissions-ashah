class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
        
            if i == len(s):
                return 0

            res = 1 + dfs(i + 1) # res without including curr char

            for j in range(i, len(s)):
                curr = s[i:j+1]
                if curr in dictionary:
                    res = min(res, dfs(j + 1))
            cache[i] = res
            return res

        return dfs(0)

            