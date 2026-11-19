class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        buy = [0] * len(prices)
        sell = [0] * len(prices)
        CD = [0] * len(prices)
        buy[0] = prices[0] * -1 # have to buy on the first day

        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], CD[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            CD[i] = max(sell[i - 1], CD[i - 1])

        return max(sell[-1], CD[-1])
        

