class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kandane's algorithm
        maxSum = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0
            total += n
            maxSum = max(total, maxSum)

        return maxSum