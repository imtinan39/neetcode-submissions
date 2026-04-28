class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap={}
        hashmap_1={}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            hashmap[s[i]]=hashmap.get(s[i],0)+1
            hashmap_1[t[i]]=hashmap_1.get(t[i],0)+1
        if hashmap==hashmap_1:
            return True
        else:
            return False
        