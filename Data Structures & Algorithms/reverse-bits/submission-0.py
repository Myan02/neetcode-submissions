class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31

        while power >= 0:
            if n & 1 == 1:
                res += 1 * (2 ** power)
            
            n = n >> 1
            power -= 1
        
        return res

        