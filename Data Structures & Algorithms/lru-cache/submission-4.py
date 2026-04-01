class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = 0
        self.right = 0
        

class LRUCache:

    def __init__(self, capacity: int):
        # hashmap that points to L.L nodes
        self.capacity = capacity
        self.cache = {}
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        
        self.lru.right = self.mru
        self.mru.left = self.lru

    # CREATE HELPER FUNCTIONS TO ADD AND REMOVE NODES FROM L.L
    def remove(self, node):
        nodeLeft = node.left
        nodeRight = node.right
        nodeLeft.right = nodeRight
        nodeRight.left = nodeLeft
    
    def add(self, node):
        mruLeft = self.mru.left
        mruLeft.right = node
        node.left = mruLeft
        self.mru.left = node
        node.right = self.mru

    def get(self, key: int) -> int:
        if key in self.cache:
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
        else:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])

            # check LRU Capacity
            if len(self.cache) > self.capacity:
                # remove lru node
                removeNode = self.lru.right
                self.remove(removeNode)
                del self.cache[removeNode.key]
      

        
