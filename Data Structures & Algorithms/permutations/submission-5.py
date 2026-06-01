class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = self.permute(nums[1:])
        prefix = nums[0]
        
        currRes = []
        for i in range(len(res)):
            for j in range(len(res[0]) + 1):
                copy = res[i].copy()
                copy.insert(j, prefix)
                currRes.append(copy)
        return currRes
