class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap={}
        ans=[]

        for i in arr:
            hashmap[i]=hashmap.get(i,0)+1
        for i in hashmap.keys():
            if hashmap[i]==1:
                ans.append(i)
        print(ans)
        print(hashmap)
        if len(ans)<k:
            return ""
        else:
            return ans[k-1]
            
        