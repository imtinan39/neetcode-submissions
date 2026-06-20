class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap={}
        l=0

        ans=0
        for r,ch in enumerate(s):
            hashmap[ch]=hashmap.get(ch,0)+1

            while (r-l+1)-max(hashmap.values())>k:
                hashmap[s[l]]-=1
                l+=1

            ans=max(ans,r-l+1)
        return ans