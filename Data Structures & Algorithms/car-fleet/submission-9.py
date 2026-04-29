class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars=sorted(zip(position,speed))
        
        time=[(target-p)/s for p,s in cars]

        stack=[]
        for i in time:
            while stack and i>=stack[-1]:
                stack.pop()
            stack.append(i)
            
        return len(stack)


        