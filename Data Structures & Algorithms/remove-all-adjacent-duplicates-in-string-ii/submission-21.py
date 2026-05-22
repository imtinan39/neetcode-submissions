class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        tmp=""
        count=0
        se=set()
        stack=[]
        hashmap={}
        for j,i in enumerate(s):
            stack.append(i)
            if len(stack)>=k:
                se = set(stack[-k:])
            hashmap[i]=hashmap.get(i,0)+1
            while stack and i==stack[-1] and hashmap[i]>=k and i in se and len(se)==1:
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

        