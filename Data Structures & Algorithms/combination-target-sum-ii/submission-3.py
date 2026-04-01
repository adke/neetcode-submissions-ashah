class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            # base case
            if total == target:
                res.append(subset.copy())
                return
            elif total > target or i == len(candidates):
                return

            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            subset.pop()

            # checking for duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)

        return res

