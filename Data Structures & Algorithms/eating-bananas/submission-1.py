class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        L, R = 1, piles[n - 1]  # 1 - 25
        rate = R


        while L <= R:
            k = (L + R) // 2
            temp_h = h

            for i in range(n):
                cur_time = math.ceil(piles[i] / k)
                temp_h -= cur_time
            
            if temp_h < 0:
                L = k + 1
            else:
                rate = k
                R = k - 1

        return rate
        