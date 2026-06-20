class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap={}
        left=0
        ans=0

        for ind,i in enumerate(s):
            hashmap[i]=hashmap.get(i,0)+1
            
            while hashmap[i]>1:
                hashmap[s[left]]-=1
                if hashmap[s[left]]==0:
                    del hashmap[s[left]]
                left+=1
            ans=max(ans,ind-left+1)
        return ans
            

        

        