class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        return first_attempt(nums, target)



def first_attempt(nums: List[int], target: int) -> List[int]:


    if len(nums) == 2:
        return [0, 1]
    
    # nums[i] == target - nums[j]
    # key = element
    # value = index
    # 3: 0, 2: 1, 
    table = {}
    for index, element in enumerate(nums):
        
        difference = target - element
        if difference in table.keys():
            return [table.get(difference), index]
        table[element] = index

        