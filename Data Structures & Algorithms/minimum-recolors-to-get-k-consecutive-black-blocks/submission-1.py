class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        res = 0
        curr = 0

        for r in range(len(blocks)):
            # reached max window size
            if k == 0:

                if blocks[l] == "W":
                    curr -= 1
                
                if blocks[r] == "W":
                    curr += 1

                l += 1
                res = min(curr, res)
                continue

            if blocks[r] == "W":
                res += 1
                curr += 1
            k -= 1
        
        return res

        
