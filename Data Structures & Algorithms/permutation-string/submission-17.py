import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dq=deque(maxlen=len(s1))
        l=0
        count=0
        hashmap={}
        for i in s1:
            hashmap[i]=hashmap.get(i,0)+1

        for  r in range(len(s2)):
            
            if s2[r] in s1:
                dq.append(s2[r])
            else:
                dq=deque(maxlen=len(s1))
            if len(dq)==len(s1):
                d2 = copy.deepcopy(hashmap)
                for d in dq:
                    if d in d2 and d2[d]!=0:
                        count+=1
                        d2[d]-=1
                    else:
                        count=0
                        break
                
                if count==len(s1) and sum(d2.values())==0:
                    return True
        return False
        