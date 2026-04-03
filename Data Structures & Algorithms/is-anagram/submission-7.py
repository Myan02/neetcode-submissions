class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = dict()

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        for char in t:
            if char in freq:
                freq[char] -= 1

                if freq[char] < 0:
                    return False

            else:
                return False


        return True
            
        