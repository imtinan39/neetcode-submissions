class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        result=[]

        for i,j in enumerate(asteroids):
            if j>0:
                stack.append(i)
            else:

                while len(stack)!=0:

                    f1=asteroids[i]
                    f2=asteroids[stack[-1]]

                    if abs(f1)==abs(f2):
                        asteroids[i]=0
                        asteroids[stack[-1]]=0
                        stack.pop()
                        break
                    elif abs(f1)<abs(f2):
                        asteroids[i]=0
                        break
                    elif abs(f1)>abs(f2):
                        asteroids[stack[-1]]=0
                        stack.pop()

        for i in asteroids:
            if i!=0:
                result.append(i)
        return result


        