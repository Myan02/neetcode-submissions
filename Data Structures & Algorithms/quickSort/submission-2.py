# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, pairs, s, e):
        if (e - s) + 1 <= 1:    # length of 1
            return
        
        pivot = pairs[e]
        left = s

        for right in range(s, e):
            if pairs[right].key < pivot.key:
                pairs[right], pairs[left] = pairs[left], pairs[right]
                left += 1
        
        pairs[left], pairs[e] = pairs[e], pairs[left]

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)


        