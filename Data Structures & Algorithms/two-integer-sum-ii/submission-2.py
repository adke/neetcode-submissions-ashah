class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # TWO-SUM PART 2
        l = 0
        r = len(numbers) - 1
        # with two pointer technique problems,
        # ensure that the indices are never OUT-OF-BOUNDS!!!

        while l < r:
            twoSum = numbers[l] + numbers[r]

            if twoSum > target:
                r -= 1
            elif twoSum < target:
                l += 1
            else:
                return [l + 1, r + 1]