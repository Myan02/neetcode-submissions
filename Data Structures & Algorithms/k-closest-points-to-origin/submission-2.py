import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for p in points:
            distance = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(minHeap, (distance, p))
        
        print(minHeap)

        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res
        