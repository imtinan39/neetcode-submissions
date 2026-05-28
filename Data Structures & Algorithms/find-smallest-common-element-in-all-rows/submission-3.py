class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hashmap={}
        ans=float("inf")

        for r in mat:
            for i in r:
                hashmap[i]=hashmap.get(i,0)+1
        
        for k in hashmap.keys():
            if hashmap[k]==len(mat):
                ans=min(ans,k)

        
        return -1 if ans==float("inf") else ans
        
      

        