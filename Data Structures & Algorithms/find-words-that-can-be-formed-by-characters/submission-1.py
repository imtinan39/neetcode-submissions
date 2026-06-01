import copy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap={}
        for i in chars:
            hashmap[i]=hashmap.get(i,0)+1
        
        ans=0
        count=0
        ans=0

        for i in words:
            dic=copy.deepcopy(hashmap)
            for r in range(len(i)):
                w=i[r]
                if w in dic:
                    count+=1
                    dic[w]-=1
                    if dic[w]==0:
                        del dic[w]
                if count==len(i) and r==len(i)-1:
                    ans+=count
                    count=0
                elif count!=len(i) and r==len(i)-1:
                    count=0
        return ans
