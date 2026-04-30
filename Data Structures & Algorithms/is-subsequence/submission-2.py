class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack=[]
        for i in s:
            stack.append(i)
        
        for i in range(len(t)-1,-1,-1):
            if stack and t[i]==stack[-1]:
                stack.pop()
        
        if stack:
            return False
        else:
           return True

        