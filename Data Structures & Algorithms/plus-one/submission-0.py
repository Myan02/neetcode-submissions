class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        while digits[i] == 9 and i > 0:
            digits[i] = 0
            i -= 1
        
        if digits[i] != 9:
            digits[i] += 1
        else:
            if i > 0:
                digits[i] = 0
                digits[i - 1] += 1
            else:
                digits[i] = 0
                digits.insert(0, 1)
        
        return digits
            

                
        