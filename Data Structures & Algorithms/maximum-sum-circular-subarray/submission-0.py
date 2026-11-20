class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        globalMin = nums[0]
        currMax = 0
        currMin = 0
        total = 0

        for n in nums:
            total += n
            currMax += n
            globalMax = max(globalMax, currMax)
            if currMax < 0:
                currMax = 0

            currMin += n
            globalMin = min(globalMin, currMin)
            if currMin > 0:
                currMin = 0
        if globalMax < 0:
            return globalMax
        else:
            return max(total - globalMin, globalMax)