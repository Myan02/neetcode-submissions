class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0   # keep track of lowest price

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            curr_price = (prices[R] - prices[L])
            res = max(curr_price, res)
        
        return res



        