class Solution:

    def encode(self, strs: List[str]) -> str:
        cipher_text = ""
        for word in strs:
            length = len(word)
            cipher_text += f"\'{length}\'{word}"
        print(cipher_text)
        return cipher_text


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            curr = ""

            # get word length
            if s[i] == '\'':
                length = ""
                i += 1
                while s[i] != '\'':
                    length += s[i]
                    i += 1
                length = int(length)

                i += 1
                j = i
                while j < (i + length):
                    curr += s[j]
                    j += 1
                res.append(curr)
                i = j
        
        return res

        



