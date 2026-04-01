class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0] # can't be 0 if it doesn't exist in nums

        while l <= r:
            if nums[r] > nums[l]:
                res = min(res, nums[l])
                return res
            else:
                mid = (l + r) // 2
                curMid = nums[mid]
                res = min(res, curMid)

                if curMid >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

        return res