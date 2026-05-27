class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        hashmap={}
        l=0
        ans=0

        for r in range(len(s)):

            if s[r] in hashmap:
                while s[r] in hashmap:
                    hashmap[s[l]]-=1
                    if hashmap[s[l]]==0:
                        del hashmap[s[l]]
                    l+=1
            hashmap[s[r]]=hashmap.get(s[r],0)+1

            if r-l+1==k:
                
                ans+=1
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                    l+=1
        return ans


        