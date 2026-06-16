class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        res = 1
        cur = s[0]
        L = 0
        freq = defaultdict(int)

        for R in range(len(s)):
            freq[s[R]] += 1
            cur = s[R] if freq[s[R]] >= freq[cur] else cur

            while L <= R and (R - L + 1) - freq[cur] > k:
                cur = s[R] if freq[s[R]] >= freq[cur] else cur
                freq[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)

        return res











        