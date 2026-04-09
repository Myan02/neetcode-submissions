# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.partition(pairs, 0, len(pairs) - 1)
        return pairs
    
    def partition(self, pairs: List[Pair], s: int, e: int):
        # only 1 element to partition
        if (e - s) + 1 <= 1:
            return 
        
        m = (s + e) // 2

        self.partition(pairs, s, m)
        self.partition(pairs, m + 1, e)

        self.merge(pairs, s, m, e)
    
    def merge(self, pairs: List[Pair], s: int, m: int, e: int):
        left = pairs[s:m+1]
        right = pairs[m+1:e+1]

        left_ptr = right_ptr = 0
        main_ptr = s

        while left_ptr < len(left) and right_ptr < len(right):
            if left[left_ptr].key <= right[right_ptr].key:
                pairs[main_ptr] = left[left_ptr]
                left_ptr += 1
            else:
                pairs[main_ptr] = right[right_ptr]
                right_ptr += 1
            main_ptr += 1
        
        while left_ptr < len(left):
            pairs[main_ptr] = left[left_ptr]
            left_ptr += 1
            main_ptr += 1
        
        while right_ptr < len(right):
            pairs[main_ptr] = right[right_ptr]
            right_ptr += 1
            main_ptr += 1







