class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        freq = collections.defaultdict(int)

        for i in range(len(nums)):
            freq[nums[i]] += 1
            if freq[nums[i]] > threshold:
                return nums[i]


        