class Listnode:
     def __init__(self, val, prev, nxt):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.count = k
        self.left = Listnode(0, None, None)
        self.right = Listnode(0, self.left, None)
        self.left.nxt = self.right


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            new = Listnode(value, self.right.prev, self.right)
            self.right.prev.nxt = new
            self.right.prev = new
            self.count -= 1
            return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            # logic
            self.left.nxt = self.left.nxt.nxt
            self.left.nxt.prev = self.left
            self.count += 1
            return True

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.left.nxt.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.nxt == self.right # this means you have no nodes in between
        

    def isFull(self) -> bool:
        return self.count == 0


        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()