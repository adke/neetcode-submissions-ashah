class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recursion problem
        res = []
        currSet = []

        def dfs(i, currTotal):
            # base case
            if i == len(nums):
                return
            elif currTotal > target:
                return
            elif currTotal == target:
                res.append(currSet.copy())
                return

            currSet.append(nums[i])
            dfs(i, currTotal + nums[i])
            currSet.pop()
            dfs(i + 1, currTotal)

        dfs(0, 0)
        return res