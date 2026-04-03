class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = len(temperatures) - 1
        stack = []
        res = []

        while r >= 0:
            if not stack:
                stack.append([temperatures[r], r])
                res.append(0)
                r -= 1
                continue
            
            if temperatures[r] < stack[-1][0]:
                stack.append([temperatures[r], r])
                res.append(1)
            else:
                while stack and temperatures[r] >= stack[-1][0]:
                    stack.pop()
                
                if not stack:
                    res.append(0)
                else:
                    res.append(stack[-1][1] - r)
                
                stack.append([temperatures[r], r])
            
            r -= 1
        
        return res[::-1]
           

            


        