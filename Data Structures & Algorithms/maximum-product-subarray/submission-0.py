class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = 1
        currMin = 1

        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
                continue
            temp = currMax
            currMax = max(n, n * currMax, n * currMin)
            currMin = min(n, n * temp, n * currMin)
            res = max(currMax, res)

        return res