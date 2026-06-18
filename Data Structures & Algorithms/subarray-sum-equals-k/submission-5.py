class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = {0:1}
        res = 0

        for i in range(len(nums)):
            total += nums[i]
            cur = total - k

            if cur in prefix:
                res += prefix[cur]

            prefix[total] = prefix.get(total, 0) + 1


        return res

            




        