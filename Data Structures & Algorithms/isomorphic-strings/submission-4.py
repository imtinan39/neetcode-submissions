class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap={}
        hashmap1={}
        arr=[]

        for i in range(len(s)):
            if s[i] not in hashmap and t[i] not in hashmap1: 
                hashmap[s[i]]=t[i]
                hashmap1[t[i]]=True
                
        st=""
        for i in range(len(t)):
            st+=hashmap.get(s[i],"ooo")
        print(st)
        return t==st
        