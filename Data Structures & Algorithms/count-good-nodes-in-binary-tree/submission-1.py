# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        def dfs(root, max_val):
            nonlocal res

            if not root:
                return 
            
            # check if current val is biggest so far on the path
            if root.val >= max_val:
                res += 1
                max_val = root.val  # update max value

            # check children nodes
            dfs(root.left, max_val)
            dfs(root.right, max_val)
        
        dfs(root, -float("inf"))
        return res
            

        