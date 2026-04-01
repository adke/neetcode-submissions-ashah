class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [amount + 1] * (amount + 1)
        arr[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if (i-c) >= 0:
                    arr[i] = min(arr[i], 1 + arr[i-c])

        if arr[amount] != (amount + 1):
            return arr[amount]
        else:
            return -1