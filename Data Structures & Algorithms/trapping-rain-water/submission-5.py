class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        max_L, max_R = 0, 0
        res = 0

        while L < R:
            max_L = max(max_L, height[L])
            max_R = max(max_R, height[R])

            if height[L] < height[R]:
                cur = min(max_L, max_R) - height[L]
                L += 1
            else:
                cur = min(max_L, max_R) - height[R]
                R -= 1
            
            res += cur
        
        return res