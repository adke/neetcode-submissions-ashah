class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        else:
            n = len(cost)
            res = [0] * (n + 1)
            res[-1] = 0
            res[-2] = cost[-1]

            for i in range(len(res) - 3, -1, -1):
                res[i] = min(cost[i] + res[i + 1], cost[i] + res[i + 2])

            return min(res[0], res[1])
