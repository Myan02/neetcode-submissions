class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R

        while L <= R:
            cur_k = (L + R) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p / cur_k)
            
            if totalTime > h:
                L = cur_k + 1
            else:
                res = cur_k
                R = cur_k - 1
        
        return res
        