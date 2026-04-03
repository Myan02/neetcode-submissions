import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency of each value, store in a dict
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1


        # build a heap based on the frequencies as the priority
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))

            # only keep at most k values
            if len(heap) > k:
                heapq.heappop(heap)
            
        # return k values from heap
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        


        