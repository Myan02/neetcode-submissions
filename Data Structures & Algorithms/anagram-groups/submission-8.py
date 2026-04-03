class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            curr_anagram = [0] * 26

            for c in s:
                curr_anagram[ord(c) - ord('a')] += 1
            
            anagrams[tuple(curr_anagram)].append(s)
        
        return list(anagrams.values())
        