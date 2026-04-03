# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        total = 0

        def hasPathSumHelper(root: Optional[TreeNode], total: int):
            if not root:
                return False
            
            total += root.val
            
            if not root.left and not root.right:
                return total == targetSum
            if hasPathSumHelper(root.left, total):
                return True
            if hasPathSumHelper(root.right, total):
                return True
            total -= root.val
            return False
        
        return hasPathSumHelper(root, total)
        
            
           
            
            
        