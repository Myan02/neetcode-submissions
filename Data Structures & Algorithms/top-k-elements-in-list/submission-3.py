class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = collections.defaultdict(int)

        # get frequencies of each number
        for num in nums:
            freq[num] += 1

        # sort keys based on value
        freq = dict(sorted(freq.items(), reverse=True, key=lambda num: num[1]))

        for key in freq.keys():
            res.append(key)
            k -= 1

            if k == 0:
                return res
            
        

        



        
        