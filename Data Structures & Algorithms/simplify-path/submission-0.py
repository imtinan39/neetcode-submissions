class Solution:
    def simplifyPath(self, path: str) -> str:
        
        arr=path.split("/")
        stack=[]
        for i in arr:
            if i=="" or i==".":
                continue
            elif i==".." and len(stack)!=0:
                stack.pop()
            elif i!="..":
                stack.append(i)
        print(stack)
        st=""
        for i in stack:
            st+="/"
            st+=i
        if st=="":
            return "/"
        else:
            return st
