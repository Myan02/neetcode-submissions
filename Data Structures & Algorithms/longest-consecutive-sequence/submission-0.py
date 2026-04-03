class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  # convert our array to a set
        longest = 0         # keep track of the longest value

        # loop through all values in the set
        for num in numSet:

            # this means start of sequence, there are no values lower than this value
            if num - 1 not in numSet:
                length = 1

                # loop through the sequence as long as there is even one value exactly one greater
                while num + length in numSet:
                    length += 1
                
                # check if the current sequence is longest
                longest = max(length, longest)
        
        return longest
                
            



