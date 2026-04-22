class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 1:
            return 0
        i = 1
        l = 0
        while i < len(prices):               # Fix 1: proper bound
            if prices[i] > prices[i - 1]:
                i += 1
            else:                             # Fix 2: else handles == case too
                profit += prices[i - 1] - prices[l]
                l = i
                i += 1
        profit += prices[i - 1] - prices[l]   # Fix 3: capture final run
        return profit