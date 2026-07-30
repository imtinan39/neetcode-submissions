class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        dic={}

        l=0
        r=0
        ans=0
        while r<len(s):
            
            dic[s[r]]=dic.get(s[r],0)+1

            if r-l+1==k:
                if len(dic)==k:
                    ans+=1
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    del dic[s[l]]
                l+=1
            
            r+=1
        return ans




        