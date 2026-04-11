class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def backtrack(i, cur, res):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in digit_map[digits[i]]:
                backtrack(i + 1, cur + c, res)
            return res
            
        if digits:
            return backtrack(0, "", [])
        
        return []
            


        
        