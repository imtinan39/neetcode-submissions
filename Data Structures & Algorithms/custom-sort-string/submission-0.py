class Solution:
    def customSortString(self, order: str, s: str) -> str:

        dic={}
        p=0
        for i in range(len(order)):
            dic[order[i]]=p
            p+=1
        
        hashmap={}

        ans=[]

        for i in s:
            hashmap[i]=hashmap.get(i,0)+1
        position=[]

        for k in dic.keys():
            if k in hashmap:
                position.append(k)
        for k in position:
            while hashmap[k]!=0:
                ans.append(k)
                hashmap[k]-=1
        for k in hashmap.keys():
            while hashmap[k]!=0:
                ans.append(k)
                hashmap[k]-=1



        return "".join(ans)
        