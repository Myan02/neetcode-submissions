# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = collections.deque()
        q.append(root)


        while q:
            cur_sublist = []
            n = len(q)

            for i in range(n):
                node = q.popleft()
                cur_sublist.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(cur_sublist)
        
        return res
                

        