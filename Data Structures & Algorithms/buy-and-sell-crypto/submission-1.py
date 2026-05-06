class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] >= prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit
