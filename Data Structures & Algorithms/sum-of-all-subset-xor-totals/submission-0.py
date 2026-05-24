class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(i, curr):
            nonlocal res
            # base case
            if i == len(nums):
                if len(curr) == 1:
                    res += curr[0]
                elif len(curr) == 0:
                    res += 0
                else:
                    currRes = 0
                    for num in curr:
                        currRes ^= num
                    res += currRes
                return

            curr.append(nums[i])
            dfs(i + 1, curr)

            curr.pop()
            dfs(i + 1, curr)

        dfs(0, [])
        return res


