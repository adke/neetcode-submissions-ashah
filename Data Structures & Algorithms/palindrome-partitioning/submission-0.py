class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        part = []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if is_palin(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        def is_palin(string, l, r):
            
            while l < r:
                
                if string[l] != string[r]:
                    return False
                l = l + 1
                r = r - 1
            
            return True

        dfs(0)
        
        return res


