class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIndex = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goalIndex:
                goalIndex = i
            
        if goalIndex == 0:
            return True
        else:
            return False