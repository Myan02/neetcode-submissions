class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm_map = defaultdict(int)
        for num in nums:
            perm_map[num] += 1
        
        res = []
        subset = []

        def permBacktracking():
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for n in perm_map:
                if perm_map[n] > 0:
                    subset.append(n)
                    perm_map[n] -= 1

                    permBacktracking()
                
                    perm_map[n] += 1
                    subset.pop()

        permBacktracking()
        return res

        