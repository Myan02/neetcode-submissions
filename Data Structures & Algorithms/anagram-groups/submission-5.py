class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                    key[ord(char) % 97] += 1
            
            table[tuple(key)].append(word)
        
        return list(table.values())
