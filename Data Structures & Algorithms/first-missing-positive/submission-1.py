class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            index = val - 1
            if index < 0 or index > len(nums) - 1:
                continue
            elif nums[index] == 0:
                nums[index] = - (len(nums) + 1)
            elif nums[index] < 0:
                continue
            else:
                nums[index] *= -1

        for i in range(1, len(nums) + 1):
            index = i - 1
            if nums[index] < 0:
                continue
            else:
                return i
        
        return len(nums) + 1
            