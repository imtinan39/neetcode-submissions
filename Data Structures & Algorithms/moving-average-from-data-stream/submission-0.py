class MovingAverage:

    def __init__(self, size: int):
        self.li=[]
        self.w=size
        
        

    def next(self, val: int) -> float:
        self.li.append(val)

        if len(self.li)<self.w:
            return sum(self.li)/len(self.li)
        else:
            return sum(self.li[-self.w:])/self.w

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
