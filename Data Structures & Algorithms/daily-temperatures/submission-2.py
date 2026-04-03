class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maintain a stack of indeces from last to first index
        # if an index is larger than the stack top, pop the top
        # if stack is empty, append 0 to result
        stack = [len(temperatures) - 1]
        result = [0]

        for i in range(len(temperatures) - 2, -1, -1):
            # keep popping the stack until you get to an index that has a larger value (or empty)
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            # append the index diff and append the index to stack
            diff = (stack[-1] - i) if stack else 0
            result.append(diff)
            stack.append(i)
        
        return result[::-1]
        

            
            


            


                
            
        