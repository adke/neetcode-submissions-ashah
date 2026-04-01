class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        sequence = 0

        for n in nums:
            if n - 1 in numSet:
                continue
            else:
                i = 1

                while n + i in numSet:
                    i += 1

                sequence = max(sequence, i)

        return sequence