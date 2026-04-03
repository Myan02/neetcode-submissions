class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            tmp = max_val
            max_val = arr[i] if arr[i] > max_val else max_val
            arr[i] = tmp
        
        arr[-1] = -1
        return arr


        