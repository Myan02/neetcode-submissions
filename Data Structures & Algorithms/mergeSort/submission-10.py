# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
    
        def partition(s, e):
            if e - s <= 0:
                return
            
            m = (s + e) // 2

            partition(s, m)
            partition(m + 1, e)

            merge(s, m, e)
        
        def merge(s, m, e):
            Left = pairs[s : m + 1]
            Right = pairs[m + 1 : e + 1]

            l, r, i = 0, 0, s

            while l < len(Left) and r < len(Right):
                if Left[l].key <= Right[r].key:
                    pairs[i] = Left[l]
                    l += 1
                else:
                    pairs[i] = Right[r]
                    r += 1
                i += 1
            
            while l < len(Left):
                pairs[i] = Left[l]
                l += 1
                i += 1
            
            while r < len(Right):
                pairs[i] = Right[r]
                r += 1
                i += 1
            
        partition(0, len(pairs) - 1)
        return pairs
            


