class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num = set(nums)

        for n in nums:
            if n - 1 in num:
                continue
            
            curr = 1

            while n + curr in num:
                curr += 1

            res = max(curr, res)

        return res