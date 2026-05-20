class Solution:
    def compress(self, chars: List[str]) -> int:

        r=len(chars)-1
        count=1
        s=""
        while r>0:
            if chars[r]==chars[r-1]:
                count+=1
                r=r-1
            else:
                if count==1:

                    s=chars[r]+s
                    r=r-1
                    count=1
                else:
                    s=chars[r]+str(count)+s

                    count=1
                    r=r-1
        if len(chars)==1:
            s=chars[0]+s
        elif count==1:
            s=chars[0]+s
        else:
            s=chars[0]+str(count)+s
        
        chars[:] = list(s)
        
        return len(chars)

        
            

        