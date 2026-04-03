class Solution:
    def maxDifference(self, s: str) -> int:
        letters = list(s)
        letters.sort()

        even = float("inf")
        odd = -float("inf")
        curr = letters[0]
        count = 0

        for elem in letters + [None]:
            if elem != curr:
                # count is even
                if count % 2 == 0:
                    even = min(count, even)
                else:
                    odd = max(count, odd)

                curr = elem
                count = 1
            else:
                count += 1
        
        # The problem asks for max(odd_freq - even_freq)
        diff = odd - even

        return int(diff)