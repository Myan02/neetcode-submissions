import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []

        for num in nums:
            freq[num] += 1
        
        freq = list(dict(sorted(freq.items(), reverse=True, key=lambda num: num[1])).keys())

        
        return freq[:k]


        