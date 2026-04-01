class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        for n in nums:
            if n - 1 in numSet:
                continue
            count = 1
            while n + count in numSet:
                count += 1
            res = max(res, count)

        return res 