class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                for j in range(i + 1, len(nums)):
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    else:
                        l = j + 1
                        r = len(nums) - 1

                        while l < r:
                            fourSum = nums[i] + nums[j] + nums[l] + nums[r]
                            if fourSum > target:
                                r -= 1
                            elif fourSum < target:
                                l += 1
                            else:
                                res.append([nums[i], nums[j], nums[l], nums[r]])
                                l += 1

                                while l < r and nums[l] == nums[l - 1]:
                                    l += 1

        return res

