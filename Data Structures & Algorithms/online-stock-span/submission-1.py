class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
            return 1
        else:
            span = 1
            while self.stack and price >= self.stack[-1][0]:
                lastPrice, lastSpan = self.stack.pop()
                span += lastSpan
            self.stack.append([price, span])
            return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)