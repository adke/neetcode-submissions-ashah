class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # need to use new algorithm here, BELLMON FORD
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp = prices.copy()
            for s, d, p in flights: # going through every edge
                if prices[s] == float("inf"):
                    continue
                elif prices[s] + p < tmp[d]:
                    tmp[d] = prices[s] + p
            prices = tmp

        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]