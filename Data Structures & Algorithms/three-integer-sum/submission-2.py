class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                tmp = nums[l] + nums[r] + nums[i]

                if tmp == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in result:
                        result.append(triplet) 
                    r -= 1 
                    l += 1
                
                elif tmp > 0:
                    r -= 1
                elif tmp < 0:
                    l += 1
        
        return result
            
        