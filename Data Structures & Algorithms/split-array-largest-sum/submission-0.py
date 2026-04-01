class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r

        def canSplit(currMax):
            subCount = 0
            currCount = 0
            for n in nums:
                currCount += n
                if currCount > currMax:
                    subCount += 1
                    currCount = n

            return subCount + 1 <= k


        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res