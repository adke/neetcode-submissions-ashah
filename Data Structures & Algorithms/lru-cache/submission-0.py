class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheHash = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, mru = self.right.prev, self.right
        prev.next = node
        mru.prev = node
        node.prev = prev
        node.next = mru


    def get(self, key: int) -> int:
        if key in self.cacheHash:
            self.remove(self.cacheHash[key])
            self.insert(self.cacheHash[key])
            return self.cacheHash[key].value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cacheHash:
            self.remove(self.cacheHash[key])
            self.cacheHash[key] = Node(key, value)
            self.insert(self.cacheHash[key])
        else:
            self.cacheHash[key] = Node(key, value)
            self.insert(self.cacheHash[key])
        
        if len(self.cacheHash) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cacheHash[lru.key]
    




        
