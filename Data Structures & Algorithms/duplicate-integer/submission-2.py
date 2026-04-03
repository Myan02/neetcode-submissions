class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # create a dict to hold all int frequencies
        frequency = dict()

        # if any value already exists in the dict, then its a dupe
        for value in nums:
            if value not in frequency:
                frequency[value] = 1
                continue
            
            return True

        
        return False

            
    
        