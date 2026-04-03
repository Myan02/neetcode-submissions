class Node():
    
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        new_node = Node(key, val)

        if not self.root:
            self.root = new_node
            return
        
        def dfs_insert(root):
            if not root:
                return new_node
            
            if new_node.key < root.key:
                root.left = dfs_insert(root.left)
            elif new_node.key > root.key:
                root.right = dfs_insert(root.right)
            else:
                root.val = new_node.val
            return root
        
        dfs_insert(self.root)


    def get(self, key: int) -> int:
        
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        
        return -1
            

    def getMin(self) -> int:
        
        min_value = 0
        def dfs_min(root):
            nonlocal min_value
            if not root:
                min_value = -1
                return
                
            if root.left:
                dfs_min(root.left)
                return 
            min_value = root.val
            return
        
        dfs_min(self.root)
        return min_value


        
    def getMax(self) -> int:

        max_value = 0
        def dfs_max(root):
            nonlocal max_value
            if not root:
                max_value = -1
                return
                
            if root.right:
                dfs_max(root.right)
                return 
            max_value = root.val
            return
        
        dfs_max(self.root)
        return max_value


    def remove(self, key: int) -> None:
        
        def dfs_remove(root, key):
            if not root:
                return None
            
            if key < root.key:
                root.left = dfs_remove(root.left, key)
            if key > root.key:
                root.right = dfs_remove(root.right, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                
                # find largest value in the left subtree
                curr = root.left
                while curr and curr.right:
                    curr = curr.right
                
                # swap root and curr values
                root.key = curr.key
                root.val = curr.val
                root.left = dfs_remove(root.left, curr.key)
            return root
        
        self.root = dfs_remove(self.root, key)
                
        


    def getInorderKeys(self) -> List[int]:
        res = []

        def dfs(root, res):
            if not root:
                return
            
            dfs(root.left, res)
            res.append(root.key)
            dfs(root.right, res)
        
        dfs(self.root, res)
        return res




