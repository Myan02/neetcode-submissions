class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        res = 0

        while L <= R:
            M = (R + L) // 2

            if M * M > x:
                R = M - 1
            elif M * M < x:
                L = M + 1
                res = M
            else:
                return M

        return res