class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow_helper(x: float, n: int) -> float:
            if n == 0:
                return 1
            
            return x * self.myPow(x, abs(n) - 1)
        
        val = pow_helper(x, n)
        return (1 / val) if (n < 0) else val
       
        
        