class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        hashmap={"}":"{",")":"(","]":"["}

        for c in s:
            if c in hashmap:
                if not stack:
                    return False
                elif hashmap[c]!=stack[-1]:
                    return False
                else:
                    stack.pop()
            
            else:
                stack.append(c)
        
        if len(stack)==0:
            return True
        else:
            return False

        