class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3

        # calculate freq of each num
        # counts index refers to value
        # counts values refers to freq
        # ex: counts([1, 0, 1, 2]) = [1, 2, 1] 
        for num in nums:
            counts[num] += 1
        
        i = 0
        for j, freq in enumerate(counts):
            for _ in range(freq):
                nums[i] = j
                i += 1
        

        


        