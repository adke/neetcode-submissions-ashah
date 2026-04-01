class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        currComb = []
        def dfs(i, currTotal):
            # BASE CASE
            if currTotal == target:
                res.append(currComb.copy())
                return
            elif i == len(candidates):
                return
            elif currTotal > target:
                return

            currComb.append(candidates[i])
            dfs(i + 1, currTotal + candidates[i])
            currComb.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, currTotal)

        dfs(0, 0)
        return res

            
