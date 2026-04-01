class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer technique
        # input must be sorted for this to work
        l = 0
        r = len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]