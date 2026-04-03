class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # three choices:
        # either both children are p and q, return self
        # one child is p or q, return that node
        # neither child is p or q, dfs down 

        def dfs(root):
            if not root:
                return None
            
            # check if values are in split branches
            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            elif p.val < root.val and q.val < root.val:
                return dfs(root.left)
            else:
                return root
        
        return dfs(root)