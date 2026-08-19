class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        res = []

        for num in nums:
            freqs[num] += 1
        
        sorted_keys = sorted(freqs.items(), key=lambda item: item[1], reverse=True)

        for num in sorted_keys[:k]:
            res.append(num[0])
        
        return res