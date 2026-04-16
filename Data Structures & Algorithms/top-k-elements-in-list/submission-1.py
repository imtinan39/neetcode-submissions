class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        result=[]
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        sort_hash=dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True)[:k])
        for i in sort_hash.keys():
            result.append(i)
        return result
             