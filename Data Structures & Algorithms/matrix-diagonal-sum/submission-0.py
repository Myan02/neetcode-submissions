class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0

        if len(mat[0]) == 1:
            return mat[0][0]
        
        if len(mat[0]) == 2:
            return sum(mat[0]) + sum(mat[1])
        
        N = len(mat)
        r, c = 0, 0
        while r != N:
            res += mat[r][c]
            r += 1
            c += 1
        
        r, c = 0, N - 1
        while r != N:
            res += mat[r][c]
            r += 1
            c -= 1
        
        return res if (N % 2) == 0 else res - mat[N // 2][N // 2]
        

            