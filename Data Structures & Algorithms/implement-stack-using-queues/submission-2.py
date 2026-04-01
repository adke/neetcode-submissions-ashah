class MyStack:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        count = 1
        while count < len(self.stack):
            currVal = self.stack.popleft()
            self.stack.append(currVal)
            count += 1
        return self.stack.popleft()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        if not len(self.stack):
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()