class Node():
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        # BST pointer to root
        self.root = None


    def insert(self, key: int, val: int) -> None:

        def insertHelper(curr_node: Node, new_node: Node) -> Node:
            # if node doesn't exist, return new node to insert
            if not curr_node:
                return new_node
            
            if new_node.key < curr_node.key:    # new node is less than root
                curr_node.left = insertHelper(curr_node.left, new_node)
            elif new_node.key > curr_node.key:  # new node is greater than root
                curr_node.right = insertHelper(curr_node.right, new_node)
            else:   # new node has the same key as curr node
                curr_node.val = new_node.val
            return curr_node

        # create a new node to insert
        new_node = Node(key, val)

        # if BST is empty, insert new node as BST root
        if not self.root:
            self.root = new_node
            return
        
        # run helper function to insert new node
        insertHelper(self.root, new_node)

        
    def get(self, key: int) -> int:
        curr = self.root
        
        # loop through BST values as long as nodes exist
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1
    
    def findMinKey(self, root) -> Node|None:
        curr = root
        
        # set curr to least value (most left value)
        while curr and curr.left:
            curr = curr.left
        
        return curr

    def getMin(self) -> int:
        min_node = self.findMinKey(self.root)
        if min_node:
            return min_node.val
        return -1

    def getMax(self) -> int:
        curr = self.root

        # set curr to max value (most right value)
        while curr and curr.right:
            curr = curr.right
        
        # if the value exists, it is the largest value
        if curr:
            return curr.val
        
        return -1

    def remove(self, key: int) -> None:

        def removeHelper(curr_node: Node, key: int) -> None:
            if not curr_node:
                return None
            
            if key < curr_node.key:
                curr_node.left = removeHelper(curr_node.left, key)
            elif key > curr_node.key:
                curr_node.right = removeHelper(curr_node.right, key)
            else:
                if not curr_node.left:
                    return curr_node.right
                if not curr_node.right:
                    return curr_node.left
                
                min_node = self.findMinKey(curr_node.right)
                curr_node.key = min_node.key
                curr_node.val = min_node.val
                curr_node.right = removeHelper(curr_node.right, min_node.key)
            return curr_node
        
        self.root = removeHelper(self.root, key)


    def getInorderKeys(self) -> List[int]:
        
        def dfs(curr_node: Node, result: List[int]):
            if not curr_node:
                return
            
            dfs(curr_node.left, result)
            result.append(curr_node.key)
            dfs(curr_node.right, result)
        
        result = []
        dfs(self.root, result)
        return result






