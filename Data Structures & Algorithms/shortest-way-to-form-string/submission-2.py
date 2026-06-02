class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        hashmap={}
        for i in source:
            hashmap[i]=hashmap.get(i,0)+1
        count=0
        r=0
        p=0
        for s in target:
            if s not in hashmap:
                return -1
            else:
                while r<len(source):
                    
                    if s==source[r]:
                        r+=1
                        p+=1
                        if r==len(source) or p==len(target):
                            count+=1
                            r=0
                        break
                    else:
                        r+=1
                    
                    if r==len(source):
                        count+=1
                        r=0
        return count

        

        