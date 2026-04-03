class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True

        L, M, R = 0, 1, 2
        flowerbed = [0] + flowerbed + [0]

        while R < len(flowerbed):
            if flowerbed[L] == 0 and flowerbed[M] == 0 and flowerbed[R] == 0:
                flowerbed[M] = 1
                n -= 1
            
            if n <= 0:
                return True
            
            L += 1
            M += 1
            R += 1

        return False