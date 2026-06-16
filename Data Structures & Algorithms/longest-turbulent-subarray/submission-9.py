class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        res = 1
        op = None
        L, R = 0, 0
        

        while R < len(arr) - 1:
            op = self.checkOpCode(arr, R)

            if not op:
                L += 1
                R += 1
                continue
            
            if op == "lesser": 
                R = self.getSubstring(arr, 0, R)
            
            else:
                R = self.getSubstring(arr, 1, R)

            res = max(res, R - L + 1)
            L = R
            
        
        return res
            
    def checkOpCode(self, arr, R):
        if R + 1 >= len(arr):
            return ""
        if arr[R] < arr[R + 1]:
            return "lesser"
        elif arr[R] > arr[R + 1]:
            return "greater"
        else:
            return ""
    
    def getSubstring(self, arr, flag, R) -> int:

        while R < len(arr) - 1:
            if flag == 0 and arr[R] < arr[R + 1]:
                R += 1
                flag = 1
            
            elif flag == 1 and arr[R] > arr[R + 1]:
                R += 1
                flag = 0
            
            else:
                break
        
        return R