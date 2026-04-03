class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # build a max heap out of stones
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        # check the root and heavier child, perform operations
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first > second:
                heapq.heappush(stones, -(first - second))


        # return final value
        stones.append(0)
        return abs(stones[0])
    