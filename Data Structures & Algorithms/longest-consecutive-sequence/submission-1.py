class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numSet = set(nums)

        for n in nums:
            if (n - 1) not in numSet:
                count = 1

                while n + count in numSet:
                    count += 1

                longest = max(longest, count)

        return longest

