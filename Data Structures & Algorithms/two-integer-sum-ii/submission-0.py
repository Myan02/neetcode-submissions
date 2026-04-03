class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        output = 0

        while l < r:
            output = numbers[l] + numbers[r]

            if output == target:
                return [l + 1, r + 1]

            if output > target:
                r -= 1
            elif output < target:
                l += 1
                
            
            
