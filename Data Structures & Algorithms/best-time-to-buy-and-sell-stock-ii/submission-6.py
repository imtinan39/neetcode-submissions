class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Key Insight:
        # We can make as many transactions as we want.
        # So just collect EVERY upward move.
        #
        # If today's price is higher than yesterday's,
        # that's free profit — take it.
        #
        # Example: [1, 3, 5]
        #   Day 0→1: 3-1 = 2  ✅ take it
        #   Day 1→2: 5-3 = 2  ✅ take it
        #   Total = 4
        #
        # This is the same as buying at 1 and selling at 5.
        # Mathematically: (5-1) = (3-1) + (5-3)
        #
        # If price drops, we just skip that day.
        # Example: [5, 3, 1]
        #   Day 0→1: 3-5 = -2  ❌ skip
        #   Day 1→2: 1-3 = -2  ❌ skip
        #   Total = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:   # price went up? take the profit
                profit += prices[i] - prices[i - 1]
        return profit