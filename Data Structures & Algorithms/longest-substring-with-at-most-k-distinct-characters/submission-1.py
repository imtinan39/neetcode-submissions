class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window=set()
        l=0
        length=0
        hashmap={}

        for r in range(len(s)):

            hashmap[s[r]]=hashmap.get(s[r],0)+1

            while len(hashmap)>k:
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l+=1
            
            length=max(length,r-l+1)
        return length
            

        