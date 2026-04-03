class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        res = [[1], [1, 1]]

        for i in range(2, numRows):

            prev = res[-1]
            curr = [1]

            L, R = 0, 1
            for _ in range(i - 1):
                curr.append(prev[L] + prev[R])
                L += 1
                R += 1
        
            curr.append(1)
            res.append(curr)
        
        return res