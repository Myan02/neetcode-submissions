class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []    # keep track of k closest points
        heap = []   # our min heap 

        """ 
        for each point, calculate the distance to (0, 0)
        store it in a heap as a tuple (distance, point)
        pair[0] is the key
        """
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            pair = (distance, point)
            heapq.heappush(heap, pair)
        
        # append the k closest values to the result
        while k:
            pair = heapq.heappop(heap)
            res.append(pair[1])
            k -= 1
        
        return res
        