class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap={}
        for i in arr:
            hashmap[i]=hashmap.get(i,0)+1

        k=[i for i in hashmap.keys() if hashmap[i]==i]
        
        if len(k)==0:
             return -1
        else:
            return max(k)
        