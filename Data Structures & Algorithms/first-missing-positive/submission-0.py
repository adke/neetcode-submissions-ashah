class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # first linear pass
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # second linear pass
        for i in range(len(nums)):
            currIndex = abs(nums[i]) - 1
            if currIndex < 0 or currIndex >= len(nums):
                continue
            elif nums[currIndex] == 0:
                nums[currIndex] = -(len(nums) + 1)
            elif nums[currIndex] < 0:
                continue
            else:
                nums[currIndex] *= -1

        # third linear pass
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
            
        return len(nums) + 1