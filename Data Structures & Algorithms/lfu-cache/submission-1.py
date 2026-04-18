class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size

    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None
        self.size -= 1

    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodeMap = {}
        self.lfuCount = 0
        self.listMap = defaultdict(LinkedList)
    
    def update(self, node):
        original = node.freq
        node.freq += 1
        self.listMap[original].pop(node)
        self.listMap[original + 1].pushRight(node)

        if original == self.lfuCount:
            if self.listMap[original].length() == 0:
                self.lfuCount += 1

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.update(node) # remove from LL under old count and add to new LL under new count
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        # two cases here we need to consider

        # 1. key already exists, so we only need to update the node in nodeMap
        # and update the listMap
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.update(node)

        if len(self.nodeMap) == self.cap:
            removeNode = self.listMap[self.lfuCount].popLeft()
            del self.nodeMap[removeNode.key]

        self.nodeMap[key] = ListNode(key, value)
        self.listMap[1].pushRight(self.nodeMap[key])
        self.lfuCount = 1


        # 2. If it's a new key, add it to nodeMap and check if capacity if reached

        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)