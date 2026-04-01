class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # find all possible solutions - backTracking
        res = []
        subset = []
        total = 0

        def dfs(i, currSubset, currTotal):
            # base case
            if currTotal == target:
                res.append(currSubset.copy())
                return
            elif currTotal > target or i == len(nums):
                return

            currSubset.append(nums[i])
            dfs(i, currSubset, currTotal + nums[i])
            subset.pop()
            dfs(i + 1, currSubset, currTotal)

        dfs(0, subset, total)

        return res
