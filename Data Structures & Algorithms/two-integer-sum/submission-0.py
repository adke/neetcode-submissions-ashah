class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbersMap = {}

        for i,n in enumerate(nums):
            currDifference = target - n

            if currDifference in numbersMap:
                return [numbersMap[currDifference], i]

            numbersMap[n] = i 