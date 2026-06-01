class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = self.permuteUnique(nums[1:])

        currRes = []
        prefix = nums[0]
        for i in range(len(res)):
            for j in range(len(res[0]) + 1):
                copy = res[i].copy()
                copy.insert(j, prefix)
                if copy not in currRes:
                    currRes.append(copy)
        return currRes