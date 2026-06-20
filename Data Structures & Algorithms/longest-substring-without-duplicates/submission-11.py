class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap={}

        count=0
        left=0
        ans=0

        for i in s:
            hashmap[i]=hashmap.get(i,0)+1
            if hashmap[i]>1:
                while hashmap[i]>1:
                    hashmap[s[left]]-=1
                    if hashmap[s[left]]==0:
                        del hashmap[s[left]]
                    left+=1
            ans=max(ans,len(hashmap))
        return ans
            

        

        