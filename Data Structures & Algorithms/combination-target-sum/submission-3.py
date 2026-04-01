class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(currRes, currTotal, i):
            # base case
            if i == len(nums):
                return
            elif currTotal > target:
                return
            elif currTotal == target:
                res.append(currRes.copy())
                return

            currRes.append(nums[i])
            dfs(currRes, currTotal + nums[i], i)
            currRes.pop()
            dfs(currRes, currTotal, i + 1)

        dfs([], 0, 0)
        return res
