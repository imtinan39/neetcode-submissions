class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=[i,1]
            else:
                hashmap[s[i]][1]=hashmap[s[i]][1]+1

        
        for i in hashmap.keys():
            if hashmap[i][1]==1:
                return hashmap[i][0]
        return -1
        