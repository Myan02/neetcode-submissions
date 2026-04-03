class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        

        def findXorSum(i, total):
            if i == len(nums):
                return total

            return findXorSum(i + 1, total ^ nums[i]) + findXorSum(i + 1, total)

        return findXorSum(0, 0)