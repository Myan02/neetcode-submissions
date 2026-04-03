class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # start with a range 1 - max(piles)
        # do binary search on the range and at every mid, check to see if we can
        #   eat the bananas in h hours
        # if we can, split the range in 2 and search the lower half
        # if we can't split the range in 2 and search the upper half

        l, r = 1, max(piles)
        rate = r
        while l <= r:
            m = (l + r) // 2

            can_eat_in_time = self.consume(piles, h, m)

            if can_eat_in_time:
                rate = m
                r = m - 1
            else:
                l = m + 1
        
        return rate

    

    def consume(self, piles: List[int], hours: int, rate: int) -> bool:
        totalTime = 0
        for p in piles:
            totalTime += math.ceil(float(p) / rate)

        if totalTime <= hours:
            return True
        return False
        
