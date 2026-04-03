class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climbStairsHelper(n: int, cache: dict) -> int:
            if n <= 1:
                return 1
            if n in cache:
                return cache[n]

            cache[n] = climbStairsHelper(n - 1, cache) + climbStairsHelper(n - 2, cache)
            return cache[n]

        return climbStairsHelper(n, {})
        