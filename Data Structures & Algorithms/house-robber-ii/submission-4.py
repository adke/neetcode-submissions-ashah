class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            nums1 = nums[1:]
            nums2 = nums[:-1]

            def houseRobber(arr):
                if len(arr) == 1:
                    return nums[0]
                elif len(arr) == 2:
                    return max(arr[0], arr[1])
                else:
                    res = [0] * len(arr)
                    res[0] = arr[0]
                    res[1] = max(arr[0], arr[1])

                    for i in range(2, len(arr)):
                        res[i] = max(res[i - 1], arr[i] + res[i - 2])
                    
                    return res[-1]

            return max(houseRobber(nums1), houseRobber(nums2))

