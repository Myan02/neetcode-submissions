class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)

        for word in strs:

            cur_key = [0] * 26

            for c in word:
                idx = ord(c) - ord("a")
                cur_key[idx] += 1
            
            keys[tuple(cur_key)].append(word)
        
        return list(keys.values())
        