# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0
            
        def dfs(root):
            nonlocal max_height
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            root_sum = left + right 
            if root_sum > max_height:
                max_height = root_sum
            return 1 + max(left, right)
        
        dfs(root)
        return max_height