class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = []

    def push(self, val: int) -> None:

        self.stack.append(val)
        
        if not self.minn:
            self.minn.append(val)
        elif val < self.minn[-1]:
            self.minn.append(val)
        else:
            self.minn.append(self.minn[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]
        
