class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack=[]
        tmp=[]

        for i in s:
            if stack and i==stack[-1][0]:
                stack[-1][1]+=1
                
            else:
                stack.append([i,1])
                
            if stack[-1][1]==k:
                stack.pop()
        

        for i in stack:
            tmp.append(i[0]*i[1])
        return "".join(tmp)


