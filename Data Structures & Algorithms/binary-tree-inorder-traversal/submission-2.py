# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def DFS(root, res):
            if not root:
                return
            
            DFS(root.left, res)
            res.append(root.val)
            DFS(root.right, res)
            return res
        res = []
        res = DFS(root, res)
        return res if root else []
            
        