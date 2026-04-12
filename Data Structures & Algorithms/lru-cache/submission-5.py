class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # dummy nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev
    
    def add(self, node):
        # always need to add to the end
        curr = self.right.prev
        node.prev = curr
        node.nxt = self.right
        curr.nxt = node
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # update linked list (curr node needs to be the MRU)
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            # evict the lru node
            evict = self.left.nxt
            self.remove(evict)
            del self.cache[evict.key]

        

        
