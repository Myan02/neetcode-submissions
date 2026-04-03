class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[-1] = -1
            return arr
        
        max_right = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            curr = arr[i]
            arr[i] = max_right
            max_right = max(max_right, curr)
        
        return arr
        