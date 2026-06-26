class Node:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self, word) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isWord = True
    
    def searchPrefix(self, c) -> bool:
        return c in self.root.children
    
    def searchWord(self, word) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord
    
    def getNode(self, c) -> Node:
        return self.root.children[c]
    
    def printTrie(self):
        
        def dfs_helper(root):
            if not root.children:
                return
            
            for c in root.children:
                print(c)
                dfs_helper(root.children[c])
        
        dfs_helper(self.root)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        ROWS, COLS = len(board), len(board[0])
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        for r in range(ROWS):
            for c in range(COLS):
                if trie.searchPrefix(board[r][c]):
                    self.backtracking(r, c, board, set(), trie.getNode(board[r][c]), [board[r][c]], res)
        
        return res
    
    def backtracking(self, r: int, c: int, board: list[list[str]], visited: set[tuple[int, int]], node: Node, substring: list[str], res: list[str]):
        
        if node.isWord:
            node.isWord = False
            res.append("".join(substring))
        
        visited.add((r, c))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (nr, nc) not in visited and board[nr][nc] in node.children:
                substring.append(board[nr][nc])
                self.backtracking(nr, nc, board, visited, node.children[board[nr][nc]], substring, res)
                substring.pop()
                
        visited.remove((r, c))

        