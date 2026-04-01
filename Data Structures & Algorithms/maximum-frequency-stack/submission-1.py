class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxVal = 0
        self.groups = defaultdict(list)

    def push(self, val: int) -> None:
        valCnt = self.count.get(val, 0) + 1
        self.count[val] = valCnt
        self.groups[valCnt].append(val)
        if valCnt > self.maxVal:
            self.maxVal = valCnt

    def pop(self) -> int:
        res = self.groups[self.maxVal].pop()
        if self.groups[self.maxVal] == []:
            self.maxVal -= 1
        self.count[res] -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
