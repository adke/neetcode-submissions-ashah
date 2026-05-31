class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = [i for i in range(1, n + 1)]
        res = []

        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i == len(candidates):
                return

            curr.append(candidates[i])
            dfs(i + 1, curr)

            curr.pop()
            dfs(i + 1, curr)

            return

        dfs(0, [])
        return res