class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        b=prices[0]
        profit=0

        for i in range(1,len(prices)):
            if prices[i]>b:
                profit=max(profit,prices[i]-b)
            elif prices[i]<b:
                b=prices[i]
        return profit

        