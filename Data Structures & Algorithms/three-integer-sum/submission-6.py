class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []     # hold the triplets here
        nums.sort()     # need to sort nums to do 2 sum 

        # since we have two pointers, we don't need to check the last 2 values
        for i, target in enumerate(nums[:len(nums) - 2]):

            # set the pointers
            l, r = i + 1, len(nums) - 1

            # if the value is greater than 0, there is no way to get to 0 as it is sorted
            if target > 0:
                break
            
            # if we have two of the same values back to back, we will get a dupe
            if nums[i] == nums[i - 1] and i > 0:
                continue
            
            # 2 sum
            while l < r:
                # check sum
                three_sum = target + nums[l] + nums[r]

                if three_sum < 0:   # increment L to get a larger sum
                    l += 1
                elif three_sum > 0: # decrement R to get a smaller sum
                    r -= 1
                else:               # sum equals 0
                    result.append([target, nums[l], nums[r]])

                    # we change both pointers because if 
                    # we only change let's say L, then our answer
                    # will always be larger than 0. If L + R = 0
                    # then L + 1 + R = 1 always
                    l += 1
                    r -= 1

                    # another check to make sure our L pointers are not the same
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result








