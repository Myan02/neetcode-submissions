class Solution:

    def encode(self, strs: List[str]) -> str:
        text = ""

        for word in strs:
            length = len(word)
            text += str(length) + "#"

            for char in word:
                text += char
                
        return text

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        i = 0
        length = ""

        while True:
            if s[i] == '#':
                i += 1
                tmp = ""
                
                for _ in range(int(length)):
                    tmp += s[i]
                    i += 1
                
                res.append(tmp)
                length = ""

                if i >= len(s):
                    break

            length += s[i]
            i += 1
        
        return res
            
            

