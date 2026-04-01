class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]: # left segment
                # 3 cases
                if target > nums[mid]:
                    l = mid + 1
                elif target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # right segment
                if target < nums[mid]:
                    r = mid - 1
                elif target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1 