class Solution:

    def encode(self, strs: List[str]) -> str:
        total_words = len(strs)
        res_str = f"{total_words}!"

        for word in strs:
            res_str += f"{len(word)}#{word}"
        
        return res_str


    # ["Hello","World"]
    # 2!5#Hello5#World
    def decode(self, s: str) -> List[str]:
        i = 0
        n = ""
        while s[i] != "!":
            n += s[i]
            i += 1

        n = int(n)
        res = [""] * n

        i += 1
        for elem in range(n):
            j = i
            while s[j] != "#":
                j += 1
            
            cur_len = int(s[i:j])
            i = j + 1
            j = i + cur_len

            res[elem] = s[i : j]
            i = j
        
        return res
    



            