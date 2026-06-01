class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)

            curr.pop()
            nextIndex = i + 1
            while nextIndex < len(nums) and nums[nextIndex] == nums[i]:
                nextIndex += 1
            dfs(nextIndex, curr)
            return

        dfs(0, [])
        return res