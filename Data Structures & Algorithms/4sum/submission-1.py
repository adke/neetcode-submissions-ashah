class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we will need 4 pointers here
        nums.sort()
        res = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                l = second + 1
                r = len(nums) - 1

                while l < r:
                    fourSum = nums[first] + nums[second] + nums[l] + nums[r]
                    if fourSum > target:
                        r -= 1
                    elif fourSum < target:
                        l += 1
                    else:
                        res.append([nums[first], nums[second], nums[l], nums[r]])
                        l += 1

                        while nums[l] == nums[l-1] and l < r:
                            l += 1
        
        return res

                