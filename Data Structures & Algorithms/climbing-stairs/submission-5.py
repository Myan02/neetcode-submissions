class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(n, memo):
            if n <= 1:
                return 1
            
            if n in memo:
                return memo[n]
            
            memo[n] = climb(n - 2, memo) + climb(n - 1, memo)
            return memo[n]
        
        return climb(n, {})

        

        