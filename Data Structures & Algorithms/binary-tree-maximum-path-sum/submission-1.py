class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(root, curr_val):
            nonlocal res

            if not root:
                return 0
            
            left = max(dfs(root.left, curr_val), 0)
            right = max(dfs(root.right, curr_val), 0)

            if root.val + left + right > res:
                res = root.val + left + right

            return root.val + max(left, right)
        
        dfs(root, root.val)
        return res