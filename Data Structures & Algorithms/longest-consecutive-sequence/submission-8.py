class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        visit = set(nums)

        for n in nums:
            curr = 0
            while n + curr in visit:
                curr += 1
            res = max(res, curr)

        return res
            