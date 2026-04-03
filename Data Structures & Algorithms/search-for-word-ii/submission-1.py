class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
    
    def getRoot(self):
        return self.root
    
    @staticmethod
    def checkLetter(letter, node):
        if letter in node.children:
            return True
        return False
    
    @staticmethod
    def getChildren(node):
        return node.children

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        create a trie out of words array
        iterate through the entire board O(n*m)
            if the char has been used before for another word, ignore it
            if a char on the board is equal to a trie root child, start dfs on that letter
        
        dfs:
            run dfs on that letter and cell position
            base cases: is the min of the row and col < 0, if it is return 
                        is the row > ROWS or col > COLS, if it is return
                        is the board[row][col] in used set, if it is return
                        is the board[row][col] equal to a child of the current tri node, if it isnt return
            loop through the children, if the current value is equal to one of the chars, recursively check that way
            also add that position to the set and result
        """

        res = []        # resulting array
        ROWS, COLS = len(board), len(board[0])  # size of board

        # create a trie for words array
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def MatrixDFS(row, col, trie_node, path, seen):
            
            # check if char on board is valid
            if min(row, col) < 0 or row >= ROWS or col >= COLS or (row, col) in seen: 
                return

            char = board[row][col]

            if char not in trie_node.children:
                return
            
            next_node = trie_node.children[char]  # get next node
            new_path = path + char
            seen.add((row, col))    # add cell to seen

            if next_node.isWord:
                res.append(new_path)
                next_node.isWord = False

            MatrixDFS(row - 1, col, next_node, new_path, seen)
            MatrixDFS(row + 1, col, next_node, new_path, seen)
            MatrixDFS(row, col - 1, next_node, new_path, seen)
            MatrixDFS(row, col + 1, next_node, new_path, seen)

            seen.remove((row, col))

        
        for row in range(ROWS):
            for col in range(COLS):
                char = board[row][col]
                
                # letter found
                if Trie.checkLetter(char, trie.getRoot()):
                    MatrixDFS(row, col, trie.getRoot(), "", set())
        
        return res
                

        
        






