# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = []
        q_ancestors = []

        def printAncestors(arr):
            for node in arr:
                print(node.val)
        
        def findAncestors(root, target, ancestors):
            if not root:
                return False

            if target.val == root.val:
                ancestors.append(root)
                return True
            
            if target.val < root.val:
                ancestors.append(root)
                if findAncestors(root.left, target, ancestors):
                    return True
                else:
                    ancestors.pop()
            

            elif target.val > root.val:
                ancestors.append(root)
                if findAncestors(root.right, target, ancestors):
                    return True
                else:
                    ancestors.pop()
            
            return False
        
        findAncestors(root, p, p_ancestors)
        findAncestors(root, q, q_ancestors)

        len_p = len(p_ancestors)
        len_q = len(q_ancestors)

        deep_child = p_ancestors if len_p > len_q else q_ancestors
        shallow_child = p_ancestors if len_p < len_q else q_ancestors

        i = len(deep_child) - 1
        j = len(shallow_child) - 1
        while i != j:
            i -= 1
        
        while True:
            if p_ancestors[i] == q_ancestors[i]:
                return p_ancestors[i]
            
            i -= 1
        




        



            

        
            

            

        
            


            











