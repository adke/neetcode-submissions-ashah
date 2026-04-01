class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # need to check if the sum of the input is an even number
        if sum(nums) % 2:
            return False
        
        total = set()
        total.add(0)

        for i in range(len(nums) - 1, -1, -1):
            currSet = set()
            for num in total:
                currSet.add(nums[i] + num)
            total.update(currSet)

        if (sum(nums) // 2) in total:
            return True
        else:
            return False


