class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maintain a stack of indeces from last to first index
        # if an index is larger than the stack top, pop the top, append the diff in the curr and top index, append the val
        # if stack is empty, append 0 to result
        stack = [len(temperatures) - 1]
        result = [0]

        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            diff = (stack[-1] - i) if stack else 0
            result.append(diff)
            stack.append(i)
        
        return result[::-1]
        

            
            


            


                
            
        