class Node: 
        def __init__(self, key, val): 
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)

        self.left.next = self.right
        self.right.prev = self.left

        self.hmap = {}
        
    def insert(self, node): 
        last = self.right.prev

        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

    def remove(self, node): 
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev 

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key]) 
            self.insert(self.hmap[key])
            return self.hmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.hmap: 
            self.remove(self.hmap[key])
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])

        if len(self.hmap) > self.cap: 
            least = self.left.next
            self.remove(least)
            del self.hmap[least.key]


        
