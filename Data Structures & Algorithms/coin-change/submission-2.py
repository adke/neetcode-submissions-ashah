class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res = [float("inf")] * (amount + 1)
        res[0] = 0

        for i in range(1, len(res)):
            for c in coins:
                if c <= i:
                    remaining = i - c
                    curRes = res[remaining] + 1
                    res[i] = min(res[i], curRes)
        
        if res[-1] == float("inf"):
            return -1
        else:
            return res[-1]

        