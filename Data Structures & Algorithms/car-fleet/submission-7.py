class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars=sorted(zip(position,speed))
        
        time=[]
        

        for p,s in cars:
            time.append((target-p)/s)

        stack=[]
        for i in time:
            while len(stack)!=0 and i>=stack[-1]:
                stack.pop()
            stack.append(i)
            
        return len(stack)


        