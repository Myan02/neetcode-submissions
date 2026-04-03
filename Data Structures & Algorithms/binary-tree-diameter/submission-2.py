# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # at ever node, keep track of the max length of the left and right nodes
        max_val = 0

        def diameter(root: Optional[TreeNode]):
            nonlocal max_val
            if not root:
                return 0
            
            left_val = diameter(root.left)
            right_val = diameter(root.right)

            max_val = max(max_val, left_val + right_val)

            return 1 + max(left_val, right_val)
        
        diameter(root)
        return max_val
        