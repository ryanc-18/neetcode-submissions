class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxP = 0
        while r < len(prices):
            # if selling price higher than buying price
            if prices[r] < prices[l]:
                l = r
                r = l

            maxP = max(maxP, prices[r] - prices[l])

            r += 1

        return maxP
        