class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            L, R = i + 1, len(nums) - 1

            while L < R:
                cur_sum = num + nums[L] + nums[R]

                if cur_sum < 0:
                    L += 1
                elif cur_sum > 0:
                    R -= 1
                else:
                    res.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
            
        return res

