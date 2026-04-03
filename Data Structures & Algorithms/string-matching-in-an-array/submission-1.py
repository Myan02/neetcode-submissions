class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        for i in range(len(word)):
            node = self.root
            
            for j in range(i, len(word)):
                letter = word[j]

                if letter not in node.children:
                    node.children[letter] = TrieNode()
                
                node = node.children[letter]
                node.count += 1
    
    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.count > 1
                    
        

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        trie = Trie()
        res = []

        for word in words: 
            trie.insert(word)
        
        for word in words:
            if trie.search(word):
                res.append(word)
        
        return res




        