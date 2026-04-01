class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        part = []

        def is_palin(string, l, r):
            
            while l < r:
                
                if string[l] != string[r]:
                    return False
                l = l + 1
                r = r - 1
            
            return True

        def dfs(i):
            if i == len(s):
                res.append(part.copy()) # want to copy the list itself
                return

            for j in range(i, len(s)):

                if is_palin(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)

        return res
