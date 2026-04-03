class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)

        for word in strs:
            word_key = [0] * 26

            for char in word:
                word_key[ord(char) - ord("a")] += 1
            
            keys[tuple(word_key)].append(word)
        
        return [words for words in keys.values()]