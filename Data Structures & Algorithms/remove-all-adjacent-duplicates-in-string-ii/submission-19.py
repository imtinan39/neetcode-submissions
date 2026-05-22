class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        tmp=""
        count=0

        stack=[]
        hashmap={}
        for j,i in enumerate(s):
            stack.append(i)
            hashmap[i]=hashmap.get(i,0)+1
            while stack and i==stack[-1] and hashmap[i]>=k:
                h=stack.pop()
                tmp=h+tmp
                count+=1
                if count==k:
                    break
            if count==k:
                hashmap[i]=hashmap[i]-count
                count=0
                tmp=""
            else:
                for t in tmp:
                    stack.append(t)
                count=0
                tmp=""

        return "".join(stack)

        