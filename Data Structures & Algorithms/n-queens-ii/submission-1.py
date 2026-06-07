class Solution:
    def totalNQueens(self, n: int) -> int:
        ROWS = n
        COLS = n
        res = 0

        cSet = set()
        pos = set()
        neg = set()

        def dfs(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(COLS):
                if c in cSet or (r + c) in pos or (r - c) in neg:
                    continue
                cSet.add(c)
                pos.add(r + c)
                neg.add(r - c)
                dfs(r + 1)
                cSet.remove(c)
                pos.remove(r + c)
                neg.remove(r - c)
            return

        dfs(0)
        return res
