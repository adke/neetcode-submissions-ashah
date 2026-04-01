class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # set up the two dummy nodes
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        # make the dummy nodes point to each other to begin with
        self.lru.nxt = self.mru
        self.mru.prev = self.lru

    # insert in linked-list as MRU
    def insert(self, node):
        prev = self.mru.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.mru
        self.mru.prev = node
    # delete node in linked-list
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # update linked-list and return value of node
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove the lru
            lruNode = self.lru.nxt
            self.remove(lruNode)
            del self.cache[lruNode.key]
