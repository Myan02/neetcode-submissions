class Node:
    def __init__(self) -> None:
        self.children = [0] * 26
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not cur.children[index]:
                cur.children[index] = Node()
            cur = cur.children[index]
        cur.isWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            index = ord(c) - ord("a")
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return True
        
        