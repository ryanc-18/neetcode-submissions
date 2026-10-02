class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers at the start, l = 0 r = 1
        l, r = 0, 1
        max_prof = 0
        while r < len(prices):
            # buy low, sell high
            if prices[l] > prices[r]:
                l = r
                r = l + 1
                # continue if selling prices greater than buying
                continue

            max_prof = max(max_prof, prices[r] - prices[l])
            r += 1

        return max_prof

            


        