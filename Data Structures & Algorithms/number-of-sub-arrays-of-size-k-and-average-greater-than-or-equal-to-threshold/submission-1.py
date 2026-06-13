class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        total = 0
        L = 0
        avg = 0

        for R in range(len(arr)):
            total += arr[R]
            
            if R - L + 1 == k:
                avg = total / k

                if avg >= threshold:
                    res += 1

                total -= arr[L]
                L += 1
            
            
        
        return res
