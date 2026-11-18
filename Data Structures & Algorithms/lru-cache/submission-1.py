class Node: 
        def __init__(self, key, val): 
            self.left = None
            self.right = None
            self.key = key
            self.val = val
            

class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity
        self.nodes = {}
        self.l = Node(0,0)
        self.r = Node(0,0)
        self.l.right, self.r.left = self.r, self.l
      
    def insert(self, node): 
        temp = self.l.right

        self.l.right = node
        node.left = self.l

        node.right = temp
        temp.left = node

        self.nodes[node.key] = node
      
    def remove(self, node): 
        temp = node.left
        node.left.right = node.right 
        node.right.left = temp 
        self.nodes.pop(node.key)
        return node
        
    def get(self, key: int) -> int:
        if key not in self.nodes: 
            return -1
        self.insert(self.remove(self.nodes[key]))
        return self.nodes[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.nodes: 
            self.remove(self.nodes[key])
            self.insert(Node(key, value))
        else: 
            self.insert(Node(key,value))
            while len(self.nodes) > self.cap: 
                self.remove(self.r.left)

        return None
