class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]

        res1 = self.helper(nums1)
        res2 = self.helper(nums2)

        return max(res1, res2)

    def helper(self, arr):
        # base case(s)
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return max(arr[0], arr[1])
        else:
            newArr = [-1] * len(arr)
            newArr[0] = arr[0]
            newArr[1] = max(arr[0], arr[1])
            # dp logic needs to be applied here
            for i in range(2, len(arr)):
                newArr[i] = max(newArr[i-1], arr[i] + newArr[i-2])

            return newArr[-1]