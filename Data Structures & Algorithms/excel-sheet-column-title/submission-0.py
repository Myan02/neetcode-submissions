class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = ""
        while columnNumber > 0:
            value = (columnNumber - 1) % 26
            res = chr(value + ord('A')) + res

            columnNumber -= value
            columnNumber //= 26
        
        return res
        

        