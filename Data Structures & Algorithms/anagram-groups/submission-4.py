class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        table = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                if key[ord(char) % 97] == 0:
                    key[ord(char) % 97] = 1
                else:
                    key[ord(char) % 97] += 1
            
            table[tuple(key)].append(word)
        
        return list(table.values())
