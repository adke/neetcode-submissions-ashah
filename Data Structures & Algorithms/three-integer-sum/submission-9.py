class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # find triplets which sum to 0
        # need to sort input for pointer technique to work
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                # two sum part 2 starts here
                l = i + 1
                r = len(nums) - 1

                while l < r:
                    threeSum = nums[i] + nums[l] + nums[r]

                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1

                        while nums[l] == nums[l-1] and l < r:
                            l += 1

        return res