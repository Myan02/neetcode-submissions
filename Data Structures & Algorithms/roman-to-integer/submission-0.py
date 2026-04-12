class Solution:
    def romanToInt(self, s: str) -> int:

        mapped = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = mapped[s[0]]

        if len(s) == 1:
            return res

        for i in range(1, len(s)):

            if mapped[s[i]] > mapped[s[i - 1]]:
                res -= mapped[s[i - 1]]
                res += mapped[s[i]] - mapped[s[i - 1]]
            else:
                res += mapped[s[i]]
        
        return res

        