class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0

        l, r = 0, 1
        while r < len(prices):
            buy = prices[l]
            if buy < prices[r]:
                profit = prices[r] - buy
                mp = max(profit, mp)
            else:
                l = r
            r += 1
        return mp