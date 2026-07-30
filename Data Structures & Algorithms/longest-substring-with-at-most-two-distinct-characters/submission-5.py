class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        length=0
        dic={}
        l=0

        for r in range(len(s)):

            dic[s[r]]=dic.get(s[r],0)+1

            while len(dic)>2:
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    del dic[s[l]]
                l+=1
            length=max(length,r-l+1)
        return length
                

