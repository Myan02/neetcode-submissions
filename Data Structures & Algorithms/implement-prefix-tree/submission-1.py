class Node:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children.keys():
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children.keys():
                return False
            cur = cur.children[c]
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children.keys():
                return False
            cur = cur.children[c]
        return True
        