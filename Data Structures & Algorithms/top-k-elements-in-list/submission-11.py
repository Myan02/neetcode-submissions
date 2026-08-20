class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = {}
        res = []

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for pair in heap:
            res.append(pair[1])
        
        return res
        

            
            