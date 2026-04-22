class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        freq=[[] for i in range(len(nums)+1)]
        result=[]
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for key,c in hashmap.items():
            freq[c].append(key)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result
             