class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            else:
                # initialize pointers
                l = i+1
                r = len(nums) - 1

                while l < r:
                    threeSum = nums[i] + nums[l] + nums[r]

                    if threeSum > 0:
                        r -= 1 # we can do this because nums is sorted
                    elif threeSum < 0:
                        l += 1 # we can do this because nums is sorted
                    else: # threeSum is 0
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1

                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        return res
            
