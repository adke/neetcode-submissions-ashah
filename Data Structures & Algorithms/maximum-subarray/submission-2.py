class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo
        res = nums[0]
        curr = 0
        for n in nums:
            curr += n
            res = max(res, curr)
            if curr < 0:
                curr = 0
        return res