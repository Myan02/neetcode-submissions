class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        res = [[1]]

        for _ in range(numRows - 1):
            prev = [0, *res[-1], 0]
            curr = []

            for i in range(1, len(prev)):
                curr.append(prev[i - 1] + prev[i])
            
            res.append(curr)
        
        return res
        