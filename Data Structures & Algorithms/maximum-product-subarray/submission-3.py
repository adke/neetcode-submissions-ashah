class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = max(nums)

        for n in nums:
            if n == 0:
                currMin = 1
                currMax = 1
                continue
            temp = n * currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            res = max(res, currMax)

        return res