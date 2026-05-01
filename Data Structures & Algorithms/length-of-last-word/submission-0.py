class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        res=s.split(" ")
        c=0
        
        for i in res:
            if len(i)!=0:
                c=len(i)
        return c

        