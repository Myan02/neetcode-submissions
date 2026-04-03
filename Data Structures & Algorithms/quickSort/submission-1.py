# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
    
    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> List[Pair]:
       # if array has 1 length (base case)
        if e - s + 1 <= 1:
            return arr
        
        
        pivot = arr[e]
        left = s
        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        
        arr[left], arr[e] = arr[e], arr[left]

        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)

        return arr
            
                



 
        