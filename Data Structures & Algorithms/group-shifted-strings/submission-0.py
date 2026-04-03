class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if len(strings) == 1:
            return [strings]
        
        keys = defaultdict(list)

        for word in strings:
            origin = ord(word[0])
            tmp = [0]

            for letter in word[1:]:
                count =  ord(letter) - origin
                tmp.append(count) if count >= 0 else tmp.append(count + 26)
            
            keys[tuple(tmp)].append(word)
        
        return list(keys.values())
            


        