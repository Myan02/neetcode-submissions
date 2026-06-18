class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(i, cur, seen, res):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            for num in nums:
                if num not in seen:
                    cur.append(num)
                    seen.add(num)
                    
                    backtracking(i + 1, cur, seen, res)

                    seen.remove(num)
                    cur.pop()

            return res
        

        seen = set()
        return backtracking(0, [], seen,  [])