class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        [1, 7, 3, 6, 5, 6]
        left = [1, 8, 11, 17, 22, 28]
        right = [6, 11, 17, 20, 27, 28]
        """

        n = len(nums)
        L, R = 0, 0

        prefix = [0]
        postfix = [0]
        
        total = 0
        for i in range(n):
            total += nums[i]
            prefix.append(total)
        
        total = 0
        for i in range(n - 1, -1, -1):
            total += nums[i]
            postfix.append(total)
        
        print(prefix)
        print(postfix)

        for i in range(n):
            pre_sum = prefix[i]
            post_sum = postfix[n - i - 1]

            if pre_sum == post_sum:
                return i
        
        return -1

        
        