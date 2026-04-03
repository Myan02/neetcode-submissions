class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []

        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            pair = (distance, point)
            heapq.heappush(heap, pair)
                
        while k:
            pair = heapq.heappop(heap)
            res.append(pair[1])
            k -= 1
        
        return res
        