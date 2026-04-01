class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge cases
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            # proceed with the bottom-up approach over here
            arr = [-1] * len(nums)
            arr[0] = nums[0]
            arr[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                arr[i] = max(arr[i-1], nums[i] + arr[i-2])

            return arr[-1]