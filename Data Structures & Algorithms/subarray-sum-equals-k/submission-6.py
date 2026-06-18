class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total_sum = 0

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            total_sum += num
            value_to_k = total_sum - k

            if value_to_k in prefix_sums.keys():
                res += prefix_sums[value_to_k]
            
            prefix_sums[total_sum] += 1
        
        return res
            




        