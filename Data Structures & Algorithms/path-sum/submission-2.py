# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case: 
            # if not root
            # if sum > targetSum
        # win condition:
            # no left or right child (leaf node)
            # sum  == targetsum
        
        if not root:
            return False
        
        def pathSum(root, cur_sum):
            if not root:
                return False
            cur_sum += root.val
            
            if not root.left and not root.right and cur_sum == targetSum:
                return True
            if pathSum(root.left, cur_sum):
                return True
            if pathSum(root.right, cur_sum):
                return True

            cur_sum -= root.val
            return False
        
        return pathSum(root, 0)
        