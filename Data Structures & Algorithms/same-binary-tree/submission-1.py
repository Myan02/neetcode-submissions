# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        root = [p, q]
        res = True

        def dfs(root: list[TreeNode, TreeNode]):
            nonlocal res
            left_tree, right_tree = root

            if not left_tree and not right_tree:
                return 
            
            if not left_tree and right_tree:
                res = False
                return
            
            if left_tree and not right_tree:
                res = False
                return
            

            dfs([left_tree.left, right_tree.left])
            if left_tree.val != right_tree.val:
                res = False
            dfs([left_tree.right, right_tree.right])
        
        dfs(root)
        return res


        