# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # initialize pointers
        s = 0                   # start of list
        e = len(pairs) - 1      # end of list

        return self.mergeSortHelper(pairs, s, e)
    
    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        # check if there is only one element left in our subarray
        sub_list_length = e - s + 1
        if sub_list_length <= 1:
            return pairs
        
        # get the middle of the sub-array by finding the average
        m = (s + e) // 2
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs
    
    def merge(self, pairs: List[Pair], s: int, m: int, e: int) -> None:
        # create lists to temporarily store our sub-arrays
        L = pairs[s:m+1]
        R = pairs[m+1:e+1]
        
        # temp list pointers
        i = 0   # pointer for L
        j = 0   # pointer for R
        
        k = s   # pointer for sub-array (use to actually update array)

        # loop through both sub-lists, stop when one of them is done
        while i < len(L) and j < len(R):
            # if left item is smaller or the same size, place left item in the main list
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            
            # if right item is smaller, place right item in the main list
            else:
                pairs[k] = R[j]
                j += 1
            
            # no matter what, something is going to be placed so iterate k to get to next value
            k += 1
        
        # if R finished first, keep going through L 
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        
        # if L finished first, keep going through R
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1
                
        
        
