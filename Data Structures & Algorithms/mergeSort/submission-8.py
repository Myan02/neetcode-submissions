# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def partition(s, e):
            if e - s + 1 <= 1:
                return 
            
            m = (e + s) // 2

            partition(s, m)
            partition(m + 1, e)

            merge(s, m, e)

        def merge(start, middle, end):
            left = pairs[start: middle + 1]
            right = pairs[middle + 1: end + 1]

            i, j, k = 0, 0, start
            while i < len(left) and j < len(right):
                if left[i].key <= right[j].key:
                    pairs[k] = left[i]
                    i += 1
                else:
                    pairs[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                pairs[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                pairs[k] = right[j]
                j += 1
                k += 1
        
        partition(0, len(pairs))
        return pairs
