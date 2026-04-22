class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices)==1:
            return 0
        i=1
        l=0
        while i<len(prices):
            if prices[i]>=prices[i-1]:
                i+=1
            elif prices[i]<prices[i-1]:   # this approach is find the valley and then the next peak. and take the differebce of peak and valley
                profit+=prices[i-1]-prices[l]
                l=i
                i=i+1
        profit += prices[i - 1] - prices[l]
        return profit