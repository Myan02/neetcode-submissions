# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [0, True]
            
            left_h = dfs(root.left)
            right_h = dfs(root.right)

            if abs(left_h[0] - right_h[0]) > 1 or not left_h[1] or not right_h[1]:
                return [-1, False]
            
            return [1 + max(left_h[0], right_h[0]), True]
        
        res = dfs(root)
        return res[1]
        