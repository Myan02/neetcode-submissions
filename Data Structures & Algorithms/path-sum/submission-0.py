# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        total = []

        def hasPathSumHelper(root: Optional[TreeNode], target: int, total: List[int]):
            if not root:
                return False
            
            total.append(root.val)
            curr_sum = sum(total)
            
            if curr_sum == target and not root.left and not root.right:
                return True
            if hasPathSumHelper(root.left, target, total):
                return True
            if hasPathSumHelper(root.right, target, total):
                return True
            total.pop()
            return False
        
        return hasPathSumHelper(root, targetSum, total)
        
            
           
            
            
        