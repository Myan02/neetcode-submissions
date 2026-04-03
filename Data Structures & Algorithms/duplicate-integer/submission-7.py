class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {num: 0 for num in nums}
        for num in nums:
            freq[num] += 1

            if freq[num] == 2:
                return True
        
        return False

        