class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # base case, only one string input
        if len(strings) == 1:
            return [strings]
        
        # key: every chars numeric distance from the word's first char
        # value: a list of valid words that fit the key
        keys = defaultdict(list)

        for word in strings:
            origin = ord(word[0])   # char to compare to
            tmp = [0]               # holds the word's key

            for letter in word[1:]:
                count =  ord(letter) - origin

                # if the char has a smaller value, add 26 to make it positive (mimics the shift)
                tmp.append(count) if count >= 0 else tmp.append(count + 26)
            
            # group all words of the same key together
            keys[tuple(tmp)].append(word)
        
        return list(keys.values())
            


        