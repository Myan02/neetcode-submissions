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
        # len of range is 1
        if (e - s) + 1 <= 1:
            return
        
        pivot = pairs[e].key
        L = s

        # partition all values < pivot
        for R in range(s, e):
            if pairs[R].key < pivot:
                pairs[R], pairs[L] = pairs[L], pairs[R]
                L += 1
        
        pairs[L], pairs[e] = pairs[e], pairs[L]

        self.quickSortHelper(pairs, s, L - 1)
        self.quickSortHelper(pairs, L + 1, e)
        

        