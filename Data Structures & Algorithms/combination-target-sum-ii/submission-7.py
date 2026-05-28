class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if i == len(candidates):
                return
            if currSum > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, currSum + candidates[i])

            # need to account for the duplicate logic here
            curr.pop()
            currIndex = i + 1
            while currIndex < len(candidates) and candidates[currIndex] == candidates[i]:
                currIndex += 1
            dfs(currIndex, curr, currSum)
            return

        dfs(0, [], 0)
        return res
