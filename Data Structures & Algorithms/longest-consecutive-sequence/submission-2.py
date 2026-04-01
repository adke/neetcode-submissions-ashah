class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0
        for n in nums:
            if n - 1 in numSet:
                continue
            else:
                currCount = 0

                while n + currCount in numSet:
                    currCount += 1

                maxCount = max(maxCount, currCount)

        return maxCount