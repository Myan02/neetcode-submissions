class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[tuple[int, int], ...] = [(temperatures[-1], len(temperatures) - 1)]
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if not stack:
                stack.append((temperatures[i], i))
            
            else:
                res[i] = stack[-1][1] - i
                stack.append((temperatures[i], i))
            
        return res

            
