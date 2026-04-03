class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        while True:
            curr = 0
            for char in str(n):
                curr += int(char) ** 2

            if curr == 1:
                return True
            
            if curr in visited:
                return False
            
            n = curr
            visited.add(n)
            