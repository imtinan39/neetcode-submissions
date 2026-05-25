class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        hashmap={}

        for i in arr:
            hashmap[i]=(abs(i-x),i)
        
        sorted_items = sorted(hashmap.items(), key=lambda item: item[1])
        res=[]
        count=0
        hashmap_2={}

        for i in arr:
            hashmap_2[i]=hashmap_2.get(i,0)+1
        
        for i in sorted_items:
            for j in range(hashmap_2[i[0]]):
                res.append(i[0])
                count+=1
                if count==k:
                    break
            if count==k:
                    break
        return sorted(res)



        