class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        
        cur_val = n & 1
        return cur_val + self.hammingWeight(n >> 1)
        