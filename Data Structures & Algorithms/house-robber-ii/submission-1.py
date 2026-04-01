class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        else:
            nums1 = nums[1:]
            nums2 = nums[:-1]

            res1 = self.helper(nums1)
            res2 = self.helper(nums2)

            return max(res1, res2)


    def helper(self, numList):
        if len(numList) == 1:
            return numList[0]
        elif len(numList) == 2:
            return max(numList[0], numList[1])
        else:
            arr = [-1] * len(numList)
            arr[0] = numList[0]
            arr[1] = max(numList[0], numList[1])

            for i in range(2, len(numList)):
                arr[i] = max(numList[i] + arr[i-2], arr[i-1])

            return arr[len(numList) - 1]


