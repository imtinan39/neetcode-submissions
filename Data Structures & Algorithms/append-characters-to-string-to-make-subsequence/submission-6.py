class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l=0
        r=0
        m=0
        while r<len(t) and l<len(s):
            if t[r]==s[l]:
                m+=1
                r+=1
                l+=1
            else:
                l+=1
        return len(t) - m


        