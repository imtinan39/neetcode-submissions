class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=[[] for i in range(len(nums)+1)]
        hashmap={}

        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for i in hashmap.keys():
            count[hashmap[i]].append(i)
        ans=[]
        l=0

        for i in range(len(count)-1,-1,-1):
            for j in count[i]:
                ans.append(j)
                l+=1
                if l==k:
                    return ans
        




        