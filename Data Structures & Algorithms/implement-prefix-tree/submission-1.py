class PrefixTree:

    class Node: 
        def __init__(self, char):
            self.val = char
            self.children = {}

        def add(node): 
            self.children[node.val] = node
            

    def __init__(self):
        self.root = self.Node('*')

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word: 
            if char in curr.children:
                curr = curr.children[char]
            else: 
                child = self.Node(char)
                curr.children[char] = child
                curr = child
        found = self.Node('*')
        curr.children["*"] = found

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char] 
            else: 
                return False
        
        if '*' in curr.children: 
            return True
        return False

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char] 
            else: 
                return False
        
        return True

