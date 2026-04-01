class Solution:
    def findMin(self, nums: List[int]) -> int:
        currMin = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:

            # first check if you are looking at numbers in increasing order
            if nums[left] < nums[right]:
                currMin = min(currMin, nums[left])
                return currMin
            # otherwise conduct the binary search logic
            else:
                mid = (left + right) // 2
                currMin = min(currMin, nums[mid])

                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

        return currMin