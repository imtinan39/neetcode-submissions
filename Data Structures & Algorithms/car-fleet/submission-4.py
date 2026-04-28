class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        hashmap={}
        for i in range(len(position)):
            hashmap[position[i]]=speed[i]
        
        position.sort()
        print(position)
        print(hashmap)
        time=[]
        print(len(position))

        for i in position:
            time.append((target-i)/hashmap[i])
        print(time)

        stack=[]
        count=0
        for i in time:
            while len(stack)!=0 and i>=stack[-1]:
                count+=1
                stack.pop()
            stack.append(i)
        return len(position)-count


        