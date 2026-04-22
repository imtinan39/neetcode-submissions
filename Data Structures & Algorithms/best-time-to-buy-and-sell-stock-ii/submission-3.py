class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        if len(prices)==1:
            return 0
        i=1
        l=0
        while l<=i and i<len(prices):
            if prices[i]>=prices[i-1]:
                i+=1
            elif prices[i]<prices[i-1]:
                profit+=prices[i-1]-prices[l]
                l=i
                i=i+1
        profit += prices[i - 1] - prices[l]
        return profit