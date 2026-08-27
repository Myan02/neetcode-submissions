class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [1, 6, 24, 48]
        # [48, 24, 12, 8]

        n = len(nums)
        left,right = [1] * n, [1] * n
        res = [1] * n

        product_ptr = 0
        cur_product = 1
        for i in range(1, n):
            cur_product *= nums[product_ptr]
            left[i] = cur_product
            product_ptr += 1
        
        product_ptr = n - 1
        cur_product = 1
        for i in range(1, n):
            cur_product *= nums[product_ptr]
            right[i] = cur_product
            product_ptr -= 1
        
        l, r = 0, n - 1
        for i in range(n):
            res[i] = left[l] * right[r]
            l += 1
            r -= 1
        
        return res

