class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        # keep track of len of each combo (end of combo means finish)
        def dfs(i, cur, res):
            if i == len(digits):
                res.append("".join(cur))
                return res
            
            for c in digit_map[digits[i]]:
                cur.append(c)
                dfs(i + 1, cur, res)

                cur.pop()
            
            return res
        
        return dfs(0, [], [])
            


        

        