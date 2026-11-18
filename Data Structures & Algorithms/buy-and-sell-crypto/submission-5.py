class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_amount = prices[0]

        for price in prices[1:]:
            if price > min_amount:
                cur_profit = price - min_amount
                max_profit = max(cur_profit, max_profit)
            else:
                min_amount = min(min_amount, price)

        return max_profit