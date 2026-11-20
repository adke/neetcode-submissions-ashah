class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = 0

        for n in nums:
            currSum += n
            res = max(currSum, res)
            if currSum < 0:
                currSum = 0
        
        return res
