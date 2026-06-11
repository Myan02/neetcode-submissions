class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31

        for _ in range(32):
            if n & 1:
                res += pow(2, power)
            
            power -= 1
            n >>= 1
        
        return res