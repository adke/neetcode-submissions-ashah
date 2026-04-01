class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # also a two pointer problem
        # more closely aligned with sliding window
        l = 0
        res = 0
        
        for r in range(1, len(prices)):
            if prices[l] >= prices[r]:
                l = r
                continue
            else:
                currProfit = prices[r] - prices[l]
                res = max(res, currProfit)

        return res
        