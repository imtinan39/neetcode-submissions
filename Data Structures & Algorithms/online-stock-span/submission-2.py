class StockSpanner:

    def __init__(self):

        self.nums=[]
        

    def next(self, price: int) -> int:
        
        stack=[]
        count=1

        for i in range(len(self.nums)-1,-1,-1):
            if self.nums[i]<=price:
                count+=1
            else:
                self.nums.append(price)
                return count
        self.nums.append(price)
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)