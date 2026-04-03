class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1

        for R in range(len(arr) - 1, -1, -1):
            tmp = arr[R]
            arr[R] = max_val
            max_val = max(max_val, tmp)
        
        return arr