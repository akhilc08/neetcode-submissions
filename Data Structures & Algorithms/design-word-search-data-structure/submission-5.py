class WordDictionary:

    class Node: 
        def __init__(self, char):
            self.val = char
            self.children = {}

        def add(self, node): 
            self.children[node.val] = node


    def __init__(self):
        self.root = self.Node('*')
        

    def addWord(self, word: str) -> None:
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
        return self.search_root(word, self.root)
    def search_root(self, word, root):
        curr = root
        for i,char in enumerate(word):
            if char == '.':
                for child in curr.children.values(): 
                    if self.search_root(word[i+1:], child): return True
                return False
            elif char in curr.children:
                curr = curr.children[char] 
            else: 
                return False
        
        if '*' in curr.children: 
            return True
        return False
        