# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []            # holds the final array
        queue = deque()     # keep track of level

        # set queue to root value to begin BFS
        if root:
            queue.append(root)
        
        # only ends when all nodes have been traversed
        while len(queue) > 0:
            
            tmp = []    # keep track if current level nodes
            for i in range(len(queue)):

                # get the current value and pop it from the queue
                curr = queue.popleft()

                tmp.append(curr.val)    # add to the level array
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            # append level array to result array
            res.append(tmp)
        
        return res

        

        