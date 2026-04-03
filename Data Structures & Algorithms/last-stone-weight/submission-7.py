class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # get two heaviest stones
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)

            if s1 < s2:
                heapq.heappush(heap, s1 - s2)
        
        heap.append(0)
        return abs(heap[0])

