# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        res = []
        
        # add root to queue
        if root:
            queue.append(root)
        
        # run as long as queue exists (or as long as there are values to traverse)
        while queue:
            # length of level
            level_size = len(queue)
            
            for i in range(level_size):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            # append the last value to the result array
            res.append(curr.val)
        
        return res
            
        