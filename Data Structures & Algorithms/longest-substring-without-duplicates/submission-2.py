class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans=0
        l=0
        hashset=set()
        hashmap={}
        for r in range(len(s)):
            if s[r] not in hashset:
                hashset.add(s[r])
                hashmap[s[r]]=r
                ans=max(ans,r-l+1)
            else:
                ans=max(ans,r-l)
                for i in range(l,hashmap[s[r]]+1):
                    hashset.remove(s[i])
                l=hashmap[s[r]]+1
                hashset.add(s[r])
                hashmap[s[r]]=r
        return ans
            
        