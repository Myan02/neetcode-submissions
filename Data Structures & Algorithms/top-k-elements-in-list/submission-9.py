class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        res = []
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        

        