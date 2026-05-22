class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        tmp=""
        count=0
        se=set()
        stack=[]
        for j,i in enumerate(s):
            stack.append(i)
            if len(stack)>=k:
                se = set(stack[-k:])
            if len(stack) >= k and i in se and len(se)==1:
                while stack and i==stack[-1]:
                    stack.pop()
                    count+=1
                    if count==k:
                        break
                if count==k:
                    count=0

        return "".join(stack)


