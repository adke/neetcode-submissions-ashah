class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recursion problem
        currTotal = 0
        res = []
        currSet = []

        def dfs(i):
            nonlocal currTotal
            # base case
            if i == len(nums):
                return
            elif currTotal > target:
                return
            elif currTotal == target:
                res.append(currSet.copy())
                return

            currSet.append(nums[i])
            currTotal += nums[i]
            dfs(i)
            currSet.pop()
            currTotal -= nums[i]
            dfs(i + 1)

        dfs(0)
        return res