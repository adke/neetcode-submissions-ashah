class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}

        for target in range(2, n + 1):
            if target == n:
                dp[target] = 0
            else:
                dp[target] = target

            for s in range(1, target): # do not include target itself
                dp[target] = max(dp[target], dp[target - s] * dp[s])

        return dp[n]

