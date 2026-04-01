class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            if n - 1 in numSet:
                continue
            else:
                counter = 1

                while n + counter in numSet:
                    counter += 1
                
                res = max(res, counter)

        return res
                