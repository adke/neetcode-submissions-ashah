class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(numss):
            # base case
            if numss == []:
                return [[]]

            perms = dfs(numss[1:])
            # nums will be [3] when perms returns [[]]
            res = []
            for perm in perms:
                for i in range(len(numss)):
                    copyPerm = perm.copy()
                    copyPerm.insert(i, numss[0])
                    res.append(copyPerm)

            return res

        return dfs(nums)