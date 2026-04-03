class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = ""

        def dfs_serialize(root):
            nonlocal res
            if not root:
                res += "#N"
                return
            
            res += f"#{root.val}"
            dfs_serialize(root.left)
            dfs_serialize(root.right)

        dfs_serialize(root)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        data = data.split("#")[1:]
        self.index = 0

        def dfs_deserialize():
            if data[self.index] == "N":
                self.index += 1
                return None
            
            node = TreeNode(int(data[self.index]))
            self.index += 1
            node.left = dfs_deserialize()
            node.right = dfs_deserialize()
            return node
        
        return dfs_deserialize()



        