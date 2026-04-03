class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0     # keep track of number of sub-arrays
        sum = 0     # keep track of window sum

        L = 0       # keep track of window L
        for R in range(len(arr)):   # keep track of window R
            # add curr value to sum
            sum += arr[R]

            # if array is at size k
            if (R - L) + 1 == k :

                # sub-array found if avg >= threshold
                if (sum / k) >= threshold:
                    res += 1
                
                # shift window to the right
                sum -= arr[L]
                L += 1
        
        return res
    
            



            

            
        
        