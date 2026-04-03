class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for element in strs:
            count = [0] * 26

            for letter in element:
                count[ord(letter) - ord('a')] += 1

            result[tuple(count)].append(element)
            print(result)
            count.clear()

        return list(result.values())




    

        