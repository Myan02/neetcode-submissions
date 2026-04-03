class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # keep track of number frequencies
        colors = [0, 0, 0]

        # count how many of each num there are, put them in the right bucket (index)
        for num in nums:
            colors[num] += 1
        
        # iterate over the colors
        i = 0   # i points to nums list
        for n in range(len(colors)):
            for j in range(colors[n]):
                nums[i] = n
                i += 1
        
        return nums

        

        