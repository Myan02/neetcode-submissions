# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) - 1

        return self.quickSortHelper(pairs, s, e)
    
    def quickSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        # check for 1 item left in sub-array
        if e - s + 1 <= 1:
            return pairs
        
        left = s

        for i in range(s, e):
            if pairs[i].key < pairs[e].key:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left += 1
        
        pairs[e], pairs[left] = pairs[left], pairs[e]

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)

        return pairs
                

        