class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0]
        rightSum = [0]

        total = 0 
        for i in range(len(nums)):
            leftSum.append(total + nums[i])
            total += nums[i]
        # print(leftSum)        

        total = 0
        for i in range(len(nums) - 1, -1, -1):
            rightSum.append(total + nums[i])
            total += nums[i]
        print(rightSum)

        for i in range(len(nums)):
            if leftSum[i] == rightSum[-2 - i]:
                return i
        
        return -1
        
        