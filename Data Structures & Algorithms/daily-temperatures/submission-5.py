class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = len(temperatures) - 1   # keep track of right index
        stack = []                  # keep track of temperature and index seen
        res = []                    # keep track of result

        while r >= 0:

            # if stack is empty, creat it
            if not stack:
                stack.append([temperatures[r], r])
                res.append(0)
                r -= 1
                continue
            
            # if you see a lower temp than the prev, append it and set the result to 1 day
            if temperatures[r] < stack[-1][0]:
                stack.append([temperatures[r], r])
                res.append(1)

            # if you see a higher temp, we keep getting rid of stack tops until we find an even higher temp
            else:
                while stack and temperatures[r] >= stack[-1][0]:
                    stack.pop()
                
                # if stack is empty, a warmer day doesnt exist
                if not stack:
                    res.append(0)
                
                # if stack is not empty, the next warmer day has been found
                else:
                    res.append(stack[-1][1] - r)
                
                stack.append([temperatures[r], r])
            
            r -= 1
        
        # return result in reverse order
        return res[::-1]
           

            


        