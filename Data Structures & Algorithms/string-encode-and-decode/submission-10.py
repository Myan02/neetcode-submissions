class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            s = f"{str(len(word))}#{word}"
            res.append(s)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            word_len = int(s[i:j])
            i = j + 1
            
            word = s[i : i + word_len]
            res.append(word)
            i += word_len
        
        return res