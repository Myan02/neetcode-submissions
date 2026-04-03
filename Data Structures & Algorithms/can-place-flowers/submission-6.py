class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False


        L, M, R = 0, 1, 2

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

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