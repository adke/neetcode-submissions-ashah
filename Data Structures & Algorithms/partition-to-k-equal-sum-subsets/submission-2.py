class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) / k 

        nums.sort(reverse=True)

        res = [[0] for i in range(k)]

        def dfs(i):
            if i == len(nums):
                return True

            seen = set()

            for j in range(k):
                if res[j][-1] in seen:
                    continue
                if res[j][-1] + nums[i] <= target:
                    seen.add(res[j][-1])
                    newTotal = res[j][-1] + nums[i]
                    res[j].append(newTotal)
                    if dfs(i + 1):
                        return True
                    res[j].pop()
            return False
        
        return dfs(0)



