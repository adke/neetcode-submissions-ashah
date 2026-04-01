class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        visit = set(nums)

        for n in nums:
            if n - 1 in visit:
                continue
            count = 0
            while n + count in visit:
                count += 1

            res = max(res, count)

        return res