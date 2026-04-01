class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalin(s, l ,r):
            while l <= r:
                if s[l] == s[r]:
                    r -= 1
                    l += 1
                else:
                    return False
            return True

        def dfs(i):
            # BASE CASE
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if isPalin(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()

            return

        dfs(0)
        return res

        