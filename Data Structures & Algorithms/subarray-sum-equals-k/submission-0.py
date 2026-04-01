class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        currSum = 0
        res = 0

        for n in nums:
            currSum += n
            currPrefix = currSum - k
            if currPrefix in prefixSum:
                res += prefixSum[currPrefix]
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        
        return res