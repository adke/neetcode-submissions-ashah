class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = {0:1}
        res = 0
        currSum = 0
        currPrefix = 0
        for n in nums:
            currSum += n
            currPrefix = currSum - k

            if currPrefix in prefixMap:
                res += prefixMap[currPrefix]

            prefixMap[currSum] = prefixMap.get(currSum, 0) + 1

        return res
