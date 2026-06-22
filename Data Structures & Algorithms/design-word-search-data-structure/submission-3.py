class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        

    def search(self, word: str) -> bool:

        def backtracking(cur, i):
            if i == len(word):
                return cur.isWord
            
            if word[i] == ".":
                for c in cur.children.values():
                    if backtracking(c, i + 1):
                        return True

                return False

            else:
                if word[i] not in cur.children:
                    return False
                return backtracking(cur.children[word[i]], i + 1)
             
        return backtracking(self.root, 0)
        
