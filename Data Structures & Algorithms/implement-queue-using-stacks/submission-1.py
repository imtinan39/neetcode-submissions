class MyQueue:

    def __init__(self):
        self.li=[]
        

    def push(self, x: int) -> None:
        self.li.append(x)
        

    def pop(self) -> int:
        self.k=self.li[0]

        for i in range(1,len(self.li)):
            self.li[i-1]=self.li[i]
        self.li.pop()
        return self.k
        

    def peek(self) -> int:

        return self.li[0]
        

    def empty(self) -> bool:

        return len(self.li)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()