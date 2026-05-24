class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l=0
        dq=deque(maxlen=len(s1))

        hash_s1={}
        for i in s1:
            hash_s1[i]=hash_s1.get(i,0)+1
        
        hash_s2={}

        for i in range(len(s2)):
            hash_s2[s2[i]]=hash_s2.get(s2[i],0)+1
            dq.append(s2[i])

            if len(dq)==len(s1):
                if hash_s2==hash_s1:
                    return True
                else:
                    hash_s2[s2[l]]-=1
                    if hash_s2[s2[l]] == 0:
                        del hash_s2[s2[l]]
                    l+=1
        return False
                
        