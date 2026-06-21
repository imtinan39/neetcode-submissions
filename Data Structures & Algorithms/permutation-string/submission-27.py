class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashset_1={}
        hashset_2={}

        l=0

        for i in s1:
            hashset_1[i]=hashset_1.get(i,0)+1

        
        for r,ch in enumerate(s2):
            hashset_2[ch]=hashset_2.get(ch,0)+1

            if r-l+1==len(s1):
                if hashset_2==hashset_1:
                    return True
                
                hashset_2[s2[l]]-=1
                if hashset_2[s2[l]]==0:
                    del hashset_2[s2[l]]
                l+=1
        return False



        
