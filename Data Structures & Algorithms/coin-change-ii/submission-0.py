class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [[0] * (amount + 1) for i in range(len(coins))]

        for r in range(len(coins)):
            arr[r][0] = 1

        for r in range(len(coins)):
            for c in range(1, amount + 1):
                if c - coins[r] >= 0:
                    arr[r][c] += arr[r][c - coins[r]]
                if r - 1 >= 0:
                    arr[r][c] += arr[r-1][c]

        return arr[len(coins) - 1][-1]
