class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            currNum = nums[mid]

            if currNum < target:
                l = mid + 1
            elif currNum > target:
                r = mid - 1
            else:
                return mid

        return - 1