class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            midVal = nums[mid]

            if midVal == target:
                return mid

            if midVal >= nums[l]:

                if target > midVal:
                    l = mid + 1
                else:
                    if target >= nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1

            else:
                if target < midVal:
                    r = mid - 1
                else:
                    if target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1

        return - 1

            
