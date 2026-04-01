class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # DFS RECURSION PROBLEM
        def dfs(vals):
            # BASE CASE
            if vals == []:
                return [[]]

            perms = dfs(vals[1:])
            res = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    copy = perm.copy()
                    copy.insert(i, vals[0])
                    res.append(copy)

            return res

        return dfs(nums)

            
