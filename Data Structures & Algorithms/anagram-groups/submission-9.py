class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        res = []
        keys = defaultdict(list)   # store char freqs as the key, word as the value

        for word in strs:
            key = [0] * 26

            for letter in word:
                idx = ord(letter) - ord('a')
                key[idx] += 1
            
            keys[tuple(key)].append(word)
        
        return list(keys.values())
