class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return first_attempt(nums, k)


def first_attempt(nums: List[int], k: int) -> List[int]:
    
    # get frequencies of each number in nums
    # key = frequency
    # value = num element 
    frequency_table = {}
    for num in nums:
        if num not in frequency_table.keys():
            frequency_table[num] = 1
            continue
        
        frequency_table[num] += 1
    
    
    frequency_list = sorted(list(frequency_table.values()), reverse=True)[:k]
    print(frequency_table)
    print()
    print(frequency_list)

    result = []
    for key, value in frequency_table.items():
        if value in frequency_list:
            result.append(key)
            frequency_list.remove(value)
            continue
    
    return result
        

    
    
        

        