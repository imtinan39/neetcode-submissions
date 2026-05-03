class MinStack:

    def __init__(self):
        self.li=[]
        self.mini=None
        

    def push(self, val: int) -> None:


        self.li.append(val)
        self.mini=min(self.li)



        
        

    def pop(self) -> None:

        self.li.pop()
        if len(self.li) !=0:
            self.mini=min(self.li)
        

    def top(self) -> int:

        return self.li[-1]
        

    def getMin(self) -> int:
        return self.mini
        
