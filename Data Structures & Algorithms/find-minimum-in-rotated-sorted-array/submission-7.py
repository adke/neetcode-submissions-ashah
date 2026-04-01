class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len (nums) - 1
        res = nums[0]

        while l <= r:

            if nums[r] > nums[l]:
                res = min(res, nums[l])
                return res

            mid = (l + r) // 2
            midVal = nums[mid]
            res = min(res, midVal)

            if midVal >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res