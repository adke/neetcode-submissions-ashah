class FreqStack:

    def __init__(self):
        self.count = {}
        self.groups = defaultdict(list)
        self.maxVal = 0
        

    def push(self, val: int) -> None:
        valCount = self.count.get(val, 0) + 1
        self.count[val] = valCount
        if valCount > self.maxVal:
            self.maxVal = valCount
        self.groups[valCount].append(val)
        
        

    def pop(self) -> int:
        val = self.groups[self.maxVal].pop()
        self.count[val] -= 1
        if self.groups[self.maxVal] == []:
            del self.groups[self.maxVal]
            self.maxVal -= 1
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()