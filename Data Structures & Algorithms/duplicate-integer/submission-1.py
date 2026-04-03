class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        return anotherAttempt(nums)

# the first attempt I thought of without considering time and space complexity
def initialAttempt(nums: List[int]) -> bool:
    
    # used to keep track of the duplicated integers
    duplicates = []

    for element in nums:
        
        # we append an element to the duplicates array one by one and if the current element exists in the duplicates list, we know there 
        # are duplicates
        if element in duplicates:
            return True
        else:
            dup.append(element)
    
    # if no duplicates are found
    return False

# this is my second attempt with time and space complexity considered
def anotherAttempt(nums: List[int]) -> bool:

    # check to see if the element exists in the rest of the list
    for elem in nums:
        if elem in nums[nums.index(elem) + 1:]:
            return True
    
    # if there are not, there are no duplicates
    return False
         