# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        # check if they are the same tree
        if self.checkSameTree(root, subRoot):
            return True
        
        # if they aren't, dfs down and try again at each node
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def checkSameTree(self, root, subRoot):
        # if both are null, we can return and try the other branch
        if not root and not subRoot:
            return True
        
        # if both are the same val and exist, try the next pair
        if root and subRoot and root.val == subRoot.val:
            return (self.checkSameTree(root.left, subRoot.left) and 
                   self.checkSameTree(root.right, subRoot.right))
        
        # if values do not match up, or nodes don't match up, return False
        return False
        
            
            

        